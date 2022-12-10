import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

def show_news_for_user():
    st.write("hi user")
def show_news_for_admin():
    st.write("hi admin")

if __name__ == '__main__':
    st.title("NYU Campus News System")
    menu = ["News", "Login", "SignUp"] 
    choice = st.sidebar.selectbox["Menu", menu]

    if choice == "News":
        st.subheader("NYU Campus News System")

    if choice == "Login":
        st.subheader("Login Section")

    if choice == "SignUp":
        st.subheader("Create New Account")