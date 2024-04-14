import streamlit as st
from PIL import Image

def type_converter():
    st.title("Image Type Converter")
    input_image = st.file_uploader("Insert your image, you want to modify",type=['png','jpg','jpeg'],accept_multiple_files=False)
    input_format = st.selectbox("Select the output format",options=['png','jpg','jpeg'])

    if st.button("Convert"):
        with Image.open(input_image) as img:
            new_name = input_image.name.split(".")[0]+'.'+input_format
            new_path = './test/'+new_name
            img = img.convert("RGB")
            img.save(f'./test/{new_name}',bitmap_format=input_format,optimize=True, quality=100)

            st.image(image=input_image)

            with open(new_path, "rb") as file:
                btn = st.download_button(
                    label="Download Image",
                    data=file,
                    file_name=f"Converted_image.{input_format}",
                    mime=f"image/{input_format}"
                )

def img_compressor():
    st.write("Still in development")

def dimention_modifier():
    st.write("Still in development")

menu = ['Image Type Converter','Image Compressor','Image Dimension Modifier']
ch = st.sidebar.selectbox("Select from the services",menu)

if ch=='Image Type Converter':
    type_converter()
elif ch=='Image Compressor':
    img_compressor()
else:
    dimention_modifier()