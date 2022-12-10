import streamlit as st
import pandas as pd
import numpy as np

def show_news_for_user():
    st.write("hi user")
def show_news_for_admin():
    st.write("hi admin")

def create_user():
    st.write("creating user...")
def check_user_exit(username, password):
    st.write("checking if user exit...")



if __name__ == '__main__':
    st.title("NYU Campus News System")
    menu = ["News", "Login", "SignUp"] 
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "News":
        st.subheader("NYU Campus News System")
        show_news_for_user

    elif choice == "Login":
        st.subheader("Login Section")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.button("Login"):
            if(check_user_exit(username, password)):
                st.success("Logged In as {}".format(username))
            else: 
                st.Warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password') 

        if st.button("Sign Up"):
            create_user(new_user, new_password)