import cv2
import easyocr
from pathlib import Path
import matplotlib.pyplot as plt

# Constants for image processing
SMALL_WIDTH_THRESHOLD = 500
MEDIUM_WIDTH_THRESHOLD = 1000
LARGE_WIDTH_THRESHOLD = 2000

# Does the output folder exist? If not, create it


def setup_output_dir(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

# Function to process each image


def process_image(image_path, reader, output_dir):
    if not Path(image_path).is_file():
        print(f"File not found: {image_path}")
        return

    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read the image: {image_path}")
        return

    detected_texts = []

    # Get bounding box predictions
    results = reader.readtext(img)

    # Draw bounding boxes and add the detected texts to the list
    for (bbox, text, prob) in results:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        detected_texts.append(text)

    all_text = ' '.join(detected_texts)
    image_width = img.shape[1]

    # Adjust font scale and thickness based on the image width
    font_scale = 1.0
    font_thickness = 1

    if SMALL_WIDTH_THRESHOLD < image_width < MEDIUM_WIDTH_THRESHOLD:
        font_scale = 1
        font_thickness = 2
    elif MEDIUM_WIDTH_THRESHOLD <= image_width < LARGE_WIDTH_THRESHOLD:
        font_scale = 2
        font_thickness = 3
    elif image_width >= LARGE_WIDTH_THRESHOLD:
        font_scale = 3
        font_thickness = 4

    # Choose text color based on image brightness
    text_color = (250, 20, 204) if img.mean() > 127 else (255, 255, 255)
    # Places it at the bottom left corner
    text_position = (10, img.shape[0] - 10)

    # Add the concatenated text to the image
    img = cv2.putText(img, all_text, text_position,
                      cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, font_thickness)

    # Convert and show the image
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_img)
    plt.axis('off')
    plt.show()

    # Save the image to the output directory
    output_path = Path(output_dir) / Path(image_path).name
    cv2.imwrite(str(output_path), img)


# Create an EasyOCR reader instance
# The language parameter is English
reader = easyocr.Reader(['en'])

# Setup the output folder
output_dir = 'output'
setup_output_dir(output_dir)

# Process each image in the assets folder
assets_dir = Path('assets')

for image_path in assets_dir.glob('*.jpg'):
    process_image(str(image_path), reader, output_dir)
