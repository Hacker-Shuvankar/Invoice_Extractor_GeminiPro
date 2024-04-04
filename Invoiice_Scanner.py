from dotenv import load_dotenv

load_dotenv()  ## load all the enviroment veriable from .env

import streamlit as st
import os  ##usefull to assign ##peeking env variable

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load Gemini pro vision

model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(input, image, prompt):  ##input = what do i want you to act like, prompt = what i am asking
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read the file into Bytes
        bytes_data = uploaded_file.getvalue()

        image_part = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_part
    else:
        raise FileNotFoundError("no file uploaded")


##initialize  streamlit app

st.set_page_config(page_title="Multi Language Invoice Extractor")

st.header("Gemini Applicaton")
input = st.text_input("Input promt : ", key="input")
uploaded_file = st.file_uploader("Choose an image of invoice...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Go for Analysis")

input_prompt = """ 
You are an expert in understanding ivoices. We will upload a image as invoice and
you will have to answer any question based on the uploaded invoice image
"""

# if submit button is click
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is -:")
    st.write(response)