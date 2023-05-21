# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data
import os
from PIL import Image

# Config
st.set_page_config(page_title='Diagrams -Image Manipulation Detection', page_icon=':📐:', layout='wide')

from data import add_logo
add_logo()
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Title
st.title('Diagrams')


# Creating dict of diagrams
list_diagram_path= os.listdir("./images/diagrams")
list_diagram_path.sort()
list_diagram_name=[]
for i in list_diagram_path:
    list_diagram_name.append(os.path.splitext(i)[0])

images_dict={"-- Select --":None}
images_dict.update(zip(list_diagram_name, list_diagram_path))
# st.write(images_dict)

user_option = st.selectbox(label="Select Diagram ",options=images_dict,index=0,label_visibility="collapsed")

if user_option == "ResNet Architecture_2":
    st.markdown("""
    <style>
    [data-testid="stImage"]{
    width:100%;height:500px;
    overflow:scroll;overflow-x:hidden;}
    </style>
    """,unsafe_allow_html=True
    )
    st.subheader(user_option)
    st.image(Image.open(os.path.join("./images/diagrams/", images_dict[user_option])))

elif images_dict[user_option] in list_diagram_path:
    st.subheader(user_option)
    st.image(Image.open(os.path.join("./images/diagrams/",images_dict[user_option])))