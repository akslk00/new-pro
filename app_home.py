import streamlit as st
import pandas as pd
from PIL import Image

def run_home_app():
    st.subheader('환영합니다!!')
    st.text('데이터를 비교하여 적합한 주택을 찾아보세요.')

    img=Image.open('./data/wnxor1.jpg')
    st.image(img)