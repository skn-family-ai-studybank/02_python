import streamlit as st

st.title("media - image")

# 서버 이미지
st.image("../data/image1.jpg")

# 웹 이미지
image_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
st.image(image_url, caption="웹 이미지")