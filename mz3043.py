import streamlit as st
import pandas as pd
import numpy as np
from configparser import ConfigParser

# -- ssh mz3043@jedi.poly.edu
# -- LOGIN: ssh mz3043@jedi.poly.edu -L 8695:localhost:8695
# -- GOTODB: psql -h localhost -U mz3043 mz3043_db
# -- 1. psql -d mz3043_db -a -f Project_demo/data/create_db.sql
# -- 2. cat Project_demo/data/customers.csv | psql -U mz3043 -d mz3043_db -c "COPY customers from STDIN CSV HEADER"
# -- 3. cat Project_demo/data/orders.csv | psql -U mz3043 -d mz3043_db -c "COPY orders from STDIN CSV HEADER"
# -- 4. ssh mz3043@jedi.poly.edu -L 8695:localhost:8695
# -- 5. streamlit run demo.py --server.address=localhost --server.port=8695

def show_news_for_user():
    st.write("hi user")
def show_news_for_admin():
    st.write("hi admin")

def create_user():
    st.write("Creating user...")
    sql_create_user = f"Select b.player_name,b.player_position,b.team_name,b.age,b.country,b.transfer_status,b.market_value,b.finishing,b.passing,b.tackling,b.handling FROM Players as a, Players as b where a.player_name='{similar_player}' and a.player_name!=b.player_name and ( a.handling=b.handling-1 or a.handling=b.handling+1 or a.handling=b.handling)"

def check_user_exit(username, password, dpt):
    st.write("Checking if user exit...")
    sql_check_user_exit = f"SELECT * FROM student WHERE username='{username}'"
    user_exit = query_db(sql_check_user_exit)["username"].tolist()
    if user_exit.size()>0:
        st.Warning("User name exits! ")
    else:
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
                show_news_for_user()
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
        type = ["Student", "Admin"]

        choice = st.selectbox("Department", dpt)
        if st.button("Sign Up"):
            create_user(new_user, new_password, dpt)