# Libraries
import streamlit as st
from PIL import Image
import os

# Confit
st.set_page_config(page_title='History', page_icon=':💾:', layout='wide')

from data import add_logo
add_logo()
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.title("History")

list_input= os.listdir("./input_img")
list_output=os.listdir("./output_img")
# st.text(list_input)
list_input.remove("ela_temp.jpg")

t1,t2=st.columns(2,gap='small')

with t1:
    t1.header("Input Images")
with t2:
    t2.header("Output Images")


for a, b in zip(list_input,list_output):
    a1,b1=st.columns(2,gap="small")
    a1.image(Image.open(os.path.join("./input_img/",a)))
    b1.image(Image.open(os.path.join("./output_img/",b)))
    st.markdown("____")