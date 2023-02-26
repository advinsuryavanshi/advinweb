import streamlit as st
import requests
import streamlit_lottie as st_lottie
from PIL import Image
import os

st.set_page_config(page_title = "MY webpage", page_icon = ":wink:", layout = "wide")

def load_lottliurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None

    return r.json()    

lottli_code = load_lottliurl("https://assets3.lottiefiles.com/packages/lf20_tfb3estd.json")

img_project1 = Image.open(os.path.join("project1.jpg"))
img_project2 = Image.open(os.path.join("project2.png"))


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css(os.path.join("style.css"))



with st.container():
    st.subheader("Hi,I am Advin Suryavanshi :wave:")
    st.title("A Machine learning enthusiast")
    st.write("I love to get my hand dirty with Data Science and Footbaal :soccer:")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            It's as complicated as writing my bumble bio but here we go.

            Hey there! My name is Advin Suryavanshi, and I'm a 3rd year computer science student with an affinity for Data Science, football and dogs. 
            I'm passionate about using data to uncover insights, and nothing gives me more joy than applying my skills to real-world problems. 
            On the weekends, I like to kick back and relax with a few games of football, and of course, a few cuddles with my furry friends. 
            I love creating Youtube videos sometimes.
            Thanks for reading, and I look forward to connecting with you! 

            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCrOcP5_i6jtONMOFE7MLy-w)")
    with right_column:
        st_lottie.st_lottie(lottli_code, height = 300, key = "coding")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")

    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project1)
    with text_column:
        st.header("Spam SMS classifier")
        st.write("""
          This project is about a Machine Learning model which classifies SMS/EMAILS in TWO categories whether a mail is spam mail or a genuine
          mail using NAIVE BAYES Machine Learning Algorithm.
        """)
        st.subheader("Tools")
        st.write("""
          Python, Streamlit, NLTK ,Sklearn, Matplotlib.pyplot, Seaborn, word cloud, collections, pickle,numpy pandas.
        """)
        st.write("[see the project](https://github.com/advinsuryavanshi/Spam_mail)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project2)
    with text_column:
        st.header("Diabetes Prediction")
        st.write("""
          Diabetes is a medical disorder that impacts how well our body uses food as fuel.Diabetes can cause blood sugar levels to rise if it is not continuously and carefully managed, 
          which raises the chance of severe side effects like heart attack and stroke. We, therefore, choose to forecast using Python machine learning.
        """)
        st.subheader("Tools")
        st.write("""
          Python, Streamlit, Sklearn, Matplotlib.pyplot, Seaborn, pickle, numpy, pandas.
        """)
        st.write("[see the project](https://github.com/advinsuryavanshi/Diabetes)")    

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """ 
    <form action="https://formsubmit.co/advin700@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder ="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>

    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()    