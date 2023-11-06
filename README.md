# Text Detection

## Description

This is a simple text detection program that uses OpenCV to detect text in an image. It uses easyOCR to which is a python module that is able to read text. It supports 80+ languages at the moment.
The program draws a bounding box around the text and displays the text in the bottom of the image. The text size is based on the size of the image, and the color of the text is based on the brightness of the image.

As you can see on the images below, it has a hard time detecting handwritten text or text that is not in a straight line. (The images are from Unsplash).

Look at [THIS PAGE](https://github.com/JaidedAI/EasyOCR) for more information on easyOCR.
Look at [THIS PAGE](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html) for more information about drawing using OpenCV.

![Text type 1](/output/img1.jpg)
![Text type 2](/output/img2.jpg)
![Text type 3: Handwritten text](/output/img3.jpg)
