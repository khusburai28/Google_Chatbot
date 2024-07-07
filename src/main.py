import streamlit as st
import PIL.Image
import textwrap
import google.generativeai as genai

GOOGLE_API_KEY = st.secrets['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)

# Title
st.title("Google-Gemini chatbot app")
st.warning("For Image input, Please Select Google gemini-pro-vision model")

# Input text box
input_text = st.text_input("Enter your prompt:")

# Image upload
img = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])

# Model selection
models = ["gemini-pro", "gemini-pro-vision"] 
selected_model = st.selectbox("Select Gemini model:", models)
print("Selected model: " + selected_model)
gp_model = genai.GenerativeModel(selected_model)

# Output text box (initially empty)
output_text = st.empty()

if st.button("Run model"):
    # Access input text and image data
    text_data = input_text
    image_data = img

    # Simulate model inference
    if selected_model == "gemini-pro":
        if text_data:
            response = gp_model.generate_content(text_data)
            result = textwrap.indent(response.text.replace('.', '*'), '> ')  
            print(result)
    elif selected_model == "gemini-pro-vision":
        if image_data and text_data:
            img_file = PIL.Image.open(image_data)
            response = gp_model.generate_content([text_data,img_file], stream=True)
            response.resolve()
            result = textwrap.indent(response.text.replace('.', '*'), '> ') 
    else:
        print("You selected different model")

    output_text.markdown(result, unsafe_allow_html=True) 


