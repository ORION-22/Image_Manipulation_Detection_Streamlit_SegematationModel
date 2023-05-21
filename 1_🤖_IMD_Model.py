import streamlit as st
from segmentation import *


st.set_page_config(page_title='Image Manipulation Detection', page_icon=':robot_face:', layout='wide')

# @st.cache_data
# def page_bg():
#     pages_bg="""
#     <style>
#     [data-testid="stAppViewContainer"]{
#     background-image:url("https://r4.wallpaperflare.com/wallpaper/542/50/545/simple-background-blue-simple-minimalism-wallpaper-6f8cd2ff7d993518a77d9204a4f35000.jpg");
#     background-size:cover;
#     }
#
#     [data-testid="stHeader"]{
#     background: rgba(0,0,0,0);
#     }
#     </style>
#     """
#     return pages_bg
#
#
# st.markdown(page_bg(),unsafe_allow_html=True)
from data import add_logo
add_logo()
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Set up the Streamlit app
st.title("Image Manipulation Detection Model ")
st.subheader("Help")
st.write("""
1. Upload the Image below 200MB
2. Image type allowed: JPG,JPEG,PNG,TIF.
3. The IMD model will show original image and other image with manipulated part approximately marked in WHITE :white_large_square:
  color and BLACK :black_large_square: part is not changed.
4. If the output Image is completely BLACK :black_large_square:, the image can be original and not tampered/manipulated.
""")



st.header("Upload an Image")
# Upload an image
uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png","tif"],)

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    img.save("input_img/" + uploaded_file.name)
    # segment_image(os.path.join("input_img/" + uploaded_file.name))



    c1,c2=st.columns(2)
    with c1:
        original_name = uploaded_file.name
        st.image(uploaded_file, caption="Original Image: " + original_name, use_column_width="auto")

    # Perform image segmentation
    with c2:
        segmented_image = segment_image(os.path.join("input_img/" + uploaded_file.name))
        st.image(segmented_image, caption="Segmented Image", use_column_width="auto")

