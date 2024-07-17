import streamlit as st
from PIL import Image
import numpy as np
import cv2
from io import BytesIO

# Function to convert an image to a watercolor sketch
def convert_to_watercolor_sketch(inp_img):
    try:
        img_1 = cv2.edgePreservingFilter(inp_img, flags=cv2.RECURS_FILTER, sigma_s=50, sigma_r=0.8)
        img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
        return img_water_color
    except cv2.error as e:
        st.error(f"Error during sketch conversion: {e}")
        return None
def pencil_sketch(inp_img):
    img_pencil_sketch, _ = cv2.pencilSketch(inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
    return img_pencil_sketch

# Function to load an image
def load_an_image(image):
    img = Image.open(image)
    return img

# Main function for the web application
def main():
    st.title('IMAGE TO SKETCH CONVERSION')
    st.subheader("Please upload your image")

    # Image file uploader
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        
        image = Image.open(image_file)
        inp_img = np.array(image)
        option = st.selectbox('How would you like to convert the image',
                             ('Convert to water color sketch',
                              'Convert to pencil sketch'))

        # Convert to watercolor sketch
        if option == 'Convert to water color sketch':
            image = Image.open(image_file)
            final_sketch = convert_to_watercolor_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png"
                )

        if option == 'Convert to pencil sketch':
            image = Image.open(image_file)
            final_sketch = pencil_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_an_image(image_file), width=250)

            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="pencilsketch.png",
                    mime="image/png"
                )

        else:
            st.warning("Sketch conversion failed. Please check your input image.")

if __name__ == '__main__':
    main()
