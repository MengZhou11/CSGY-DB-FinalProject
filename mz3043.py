import streamlit as st
import pandas as pd
import numpy as np

def show_news_for_user():
    st.write("hi user")
def show_news_for_admin():
    st.write("hi admin")

def create_user():
    st.write("Creating user...")
    sql_create_user = f"Select b.player_name,b.player_position,b.team_name,b.age,b.country,b.transfer_status,b.market_value,b.finishing,b.passing,b.tackling,b.handling FROM Players as a, Players as b where a.player_name='{similar_player}' and a.player_name!=b.player_name and ( a.handling=b.handling-1 or a.handling=b.handling+1 or a.handling=b.handling)"
def check_user_exit(username, password):
    st.write("Checking if user exit...")
    sql_check_user_exit = f"SELECT username FROM student WHERE username='{username}' AND password='{password}'"
    if(sql_check_user_exit==username):
        st.write("You have logged in as {username}")
        return True
    return False



if __name__ == '__main__':
    st.title("NYU Campus News System")
    menu = ["News", "Login", "SignUp"] 
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "News":
        st.subheader("NYU Campus News System")
        show_news_for_user()

    elif choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            if(check_user_exit(username, password)):
                st.success("Logged In as {}".format(username))
            else: 
                st.Warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password') 
        dpt = ["Applied Physics", "Biomedical Engineering", "Center for Urban Science and Progress", "Chemical and Biomolecular Engineering",
        "Civil and Urban Engineering", "Computer Science and Engineering", "Electrical and Computer Engineering",
        "Finance and Risk Engineering", "Mathematics", "Mechanical and Aerospace Engineering", "Technology, Culture and Society", 
        "Technology Management and Innovation"]
        choice = st.selectbox("Department", dpt)

        if st.button("Sign Up"):
            create_user(new_user, new_password)