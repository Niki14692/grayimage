import streamlit as st
from PIL import Image

st.subheader("Colour to Grayscale Converter")

with st.expander("Start Camera"):
   camara_image = st.camera_input("Camera")

with st.expander("Drag and grop file here"):
    upload_image = st.file_uploader("Upload Image")

if camara_image:
    img = Image.open(camara_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

if upload_image:
    img1 = Image.open(upload_image)
    gray_camera_img1 = img1.convert('L')
    st.image(gray_camera_img1)
