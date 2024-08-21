


# Configure Gemini AI model with the provided API key


# Function to get response from Gemini A






#########################


import streamlit as st
import google.generativeai as genai
from api_key import api_key
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
# Load environment variables


genai.configure(api_key=api_key)


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="AI-ATS",
    page_icon="robot",
    layout="centered",
)

# Function to configure Gemini AI model with the provided API key
def configure_gemini_api(api_key):
    genai.configure(api_key=api_key)

# Configure Gemini AI model with the provided API key


# Function to get response from Gemini AI
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF file


# Prompt Template
input_prompt = """
    You are a domain expert in medical image analysis. You are tasked with 
    examining medical images for a renowned hospital.
    Your expertise will help in identifying or 
    discovering any anomalies, diseases, conditions or
    any health issues that might be present in the image.

    Your key responsibilites:
    1. Detailed Analysis : Scrutinize and thoroughly examine each image, 
    focusing on finding any abnormalities.
    2. Analysis Report : Document all the findings and 
    clearly articulate them in a structured format.
    3. Recommendations : Basis the analysis, suggest remedies, 
    tests or treatments as applicable.
    4. Treatments : If applicable, lay out detailed treatments 
    which can help in faster recovery.

    Important Notes to remember:
    1. Scope of response : Only respond if the image pertains to 
    human health issues.
    2. Clarity of image : In case the image is unclear, 
    note that certain aspects are 
    'Unable to be correctly determined based on the uploaded image'
    3. Disclaimer : Accompany your analysis with the disclaimer: 
    "Consult with a Doctor before making any decisions."
    4. Your insights are invaluable in guiding clinical decisions. 
    Please proceed with the analysis, adhering to the 
    structured approach outlined above.

    Please provide the final response with these 4 headings : 
    Detailed Analysis, Analysis Report, Recommendations and Treatments


"""

## app

st.title("Visual Medical Assistant 👨‍⚕️ 🩺 🏥")
st.subheader("Pani ka nahi hota hai 'taste', YE App Hai 'AI' Based'   ")
st.title("Made By AMAN SANDE")
st.subheader("An app to help with medical analysis using images")


###
file_uploaded = st.file_uploader('Upload the image for Analysis',
                                 type=['png', 'jpg', 'jpeg','heic','pdf'])

if file_uploaded:
    st.image(file_uploaded, width=200, caption='Uploaded Image')

submit = st.button("Generate Analysis")

if submit:

    image_data = file_uploaded.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpg",
            "data": image_data
        }
    ]


    prompt_parts = [
        image_parts[0],
        system_prompts[0],
    ]



    response = model.generate_content(prompt_parts)
    if response:
        st.title('Detailed analysis based on the uploaded image')
        st.write(response.text)
