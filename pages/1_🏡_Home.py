# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='Home -Image Manipulation Detection', page_icon=':house_with_garden:', layout='wide')

from data import add_logo
add_logo()
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.markdown("""
    <style type="text/css">
    div[data-testid="stImage"] {
        border:10px;
        padding:30px;
        border-radius: 10px;
        background:#FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.title('Image Manipulation Detection Using CNN')

# st.header("Problem")
# st.write(
#     """
#     <div style="text-align:justify;font-size:17px">
#
#     </div>
#     """,
#     unsafe_allow_html=True)
# st.markdown('#')

# Content
st.write(
    """ 
    <div style="text-align:justify;font-size:19px;">
    Welcome to our project website on <b><i>Image Manipulation Detection!</i></b> To identify various forms of picture manipulation, 
    such as copy-move forgery, splicing forgery, and retouching/filtering, we employ cutting-edge machine learning 
    models. To achieve higher accuracy and durability, our models combine the strength of U-Net and ResNet. To find 
    out more about the approaches, model architecture, and training methods, scroll down our website. Through 
    interactive demos and side-by-side comparisons, see how successful our models are. Join us in preventing fake 
    digital images so that the internet is reliable and safe.
    </div>
    """,
    unsafe_allow_html=True)
st.markdown('#')

st.subheader("Problem")
st.write(
    """
    <div style="text-align:justify;font-size:17px">
    In the vast realm of digital imagery, a dark shadow looms: image manipulation. It's a cunning art that distorts 
    reality, spreading misinformation and deceiving unsuspecting eyes. Conventional methods, shackled by their limited 
    prowess, struggle to unmask the intricately woven illusions of skillful manipulators. Hence, the call for an 
    imaginative intervention, where deep learning dances harmoniously with creativity, emerges.
    </div>
    """,
    unsafe_allow_html=True)
st.markdown('#')

st.subheader("Solution")
st.write(
    """
    <div style="text-align:justify;font-size:17px">
    Our solution uses ResNet and U-Net, advanced deep learning models, to detect image manipulations. ResNet 
    identifies overall manipulations by capturing global features, while U-Net highlights local tampered regions. 
    With extensive training on diverse datasets, our models accurately detect copy-move and splicing forgeries. 
    By integrating ResNet and U-Net, our solution ensures trust in visual content, empowering users to verify 
    authenticity and maintain reliability in the digital realm.
    </div>
    """,
    unsafe_allow_html=True)
st.markdown('#')

c3,c4= st.columns(2)
c3.image(Image.open('./images/realputin.png'))
c4.image(Image.open('./images/fakeputin.png'))
st.markdown('#')
st.write(
    """
    <div style="text-align:justify;font-size:17px">
    Image manipulation detection techniques play a crucial role in addressing the proliferation of digitally manipulated
     images.One notable example is the manipulation of images featuring prominent figures such as political leaders. One example is putting Putin in the middle of a picture when he wasn't there before. These fabrications might be made to provide a misleading narrative or to impact how the public sees a person's power or influence.
    </div>
    """,
    unsafe_allow_html=True)

st.markdown('#')
c1, c2= st.columns(2)
c1.image(Image.open('./images/realmodi1.png'))
c2.image(Image.open('./images/fakemodi1.png'))


st.markdown('#')
st.write(
    """
    <div style="text-align:justify;font-size:17px">
    
    Let's consider another example where an image of political leaders like Narendra Modi and Amit Shah is 
    manipulated to show them wearing Muslim hats. Such an image can be intentionally created to spread misinformation, 
    provoke controversy, or manipulate public perception. 
    </div>
    """,
    unsafe_allow_html=True)


st.markdown('#')
st.subheader('Methodology')
st.write(
    """
     <div style="text-align:justify;font-size:17px">
    In our model to detect image manipulation, we use a combination of ResNet and Unet. The Resnet network allows the 
    network to learn efficiently from deeper layers and capture more complex features while the Unet architecture helps 
    the model to capture the underlying manipulated regions quickly and works efficiently even on small training 
    datasets. Here is a general approach that is followed in our methodology:
    <ol>
    <li>Image Resizing: The very first step is to resize the images in the dataset to a standard size and color format 
    which helps us to train the model efficiently.</li>
    <li>Error Level Analysis: Error Level Analysis (ELA) is a technique which examines the difference in compression 
    quality between different regions of an image. By calculating the error levels between the original and recompressed
     versions, areas of the image with significant manipulation or tampering can be identified. ELA can help reveal 
     inconsistencies in compression artifacts and highlight potential areas of image manipulation for further investigation.</li>
    <li>Processing: Following pre-processing, we build the model using the most appropriate parameters, train it, 
    then test it using the dataset. The model is prepared for use in real-world circumstances after testing is finished. 
    The programme then outputs a predicted mask of the input image that emphasises the edited areas. These regions can 
    be compared to the areas of the image that were actually altered and included in the dataset.</li>
    
    After completing all of these processes, the model is prepared for usage with real-world photos, where it can assist in resolving a number of issues brought on by modified photographs (such as fraudulent images on social media or news websites).
    </div>
    """,
    unsafe_allow_html=True)
st.image("images/Method_ela.png")
st.markdown('#')

st.subheader('Future Works')
st.write(
    """
    <div style="text-align:justify;font-size:17px">
    The future work may focus on increasing the accuracy rate of the proposed algorithm in images as well as in video forgery detection. Another future direction in the proposed system can be of using a variable size of overlapping blocks which are used for the morphological operations(image processing operations that process images based on shapes and blocks of pixels). The usage of this system is generally limited to the forensics, in future this system can also be implemented to filter out the content on the social media to eliminate fake news and malicious content.
    </div>
    """,
    unsafe_allow_html=True)
st.markdown("#")

st.subheader("Team Members:")
t1,t2 =st.columns(2)
with t1:
    t1.write("<h4>AISSMS's Institute of Information Technology, Pune</h4>",unsafe_allow_html=True)
with t2:
    t2.write(
        """
        Made By: 
        <div style="text-align:justify;font-size:20px">
        <ul><b>
        <li>Onasvee Banarse</li>
        <li>Kaustubh Kabra</li>
        <li>Harsh Shah</li>
        <li>Akash Mete</li>
        </ul>
        
        </div>
        """,
        unsafe_allow_html=True)
st.markdown("#")

c1, c2, c3 = st.columns(3)
with c1:
    st.info('**[Email](mailto:onasvee.banarase@aissmsioit.org)**', icon="📧")
with c2:
    st.info('**[GitHub](https://github.com/ORION-22/Image_Manipulation_Detection_Streamlit_SegematationModel)**', icon="💻")

