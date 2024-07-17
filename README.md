# Image-to-Sketch-Conversion-app-using-Streamlit
Converts images to watercolor and pencil sketches using OpenCV and Streamlit.
# Project Overview
## Goal
The goal of this project is to create a web application that allows users to upload an image and convert it into either a watercolor sketch or a pencil sketch.

## Technologies Used

**1. Streamlit:**
- Streamlit is a Python library for creating interactive web applications with minimal effort.
- Why Streamlit? It provides an easy way to build data-driven apps without extensive web development knowledge.

**2. OpenCV (Open Source Computer Vision Library):**
- OpenCV is a powerful library for computer vision and image processing.
- Why OpenCV? It offers a wide range of image manipulation functions, making it ideal for sketch conversion.

**3. PIL (Python Imaging Library):**
- PIL (now known as Pillow) is used for opening, manipulating, and saving image files.
- Why PIL? It’s a straightforward library for handling image data.

## Sketch Conversion Process
**1. User Uploads an Image:**
- Users can upload an image (in formats like PNG, JPG, or JPEG) through the web interface.

**2. Image Processing:**
- The uploaded image is converted into a NumPy array.
- We apply edge-preserving filters using OpenCV to create a watercolor-like effect.
- Alternatively, we can create a pencil sketch using OpenCV’s pencilSketch function.

**3. Display the Result:**
- The resulting sketch (either watercolor or pencil) is displayed to the user on the web page.

**4. Download Option:**
- Users can download the converted sketch as an image file (e.g., JPEG).
## How to Run the Web Application
**1. Install the required libraries:**
> pip install streamlit opencv-python-headless pillow

**2. Create a Python script (e.g., app.py) with the code you’ve written.**
- Make sure to structure it as a Streamlit app.
- Define functions for sketch conversion and image loading.
**3. Run the app:**
> streamlit run app.py

- Access the app in your web browser (usually at http://localhost:8501).
