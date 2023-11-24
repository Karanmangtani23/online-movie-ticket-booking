import streamlit as st
import database as db
from booking import booking
from movies import movies
from shows import shows
from prices import prices
from screens import screens
from execute import execute
st.set_page_config(layout='wide')

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()

def show_main_page():
    st.sidebar.title(f"Welcome {st.session_state['name']}")
    st.sidebar.button("Logout",on_click=LoggedOut_Clicked)
    with mainSection:
         vb,am,ss,ap,sc,ex  = mainSection.tabs(["View Bookings","Alter Movies","Schedule Shows","Alter Price","Alter Screens","Execute"])
    with vb:
        booking()
    with am:
        movies()
    with ss:
        shows()
    with ap:
        prices()
    with sc:
        screens()
    with ex:
        execute()
 
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def LoggedIn_Clicked(userName, password):
    val,name = db.login(userName, password)
    if val:    
        st.session_state['loggedIn'] = True
        st.session_state['name'] = name
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="User-Id", value="", placeholder="Enter your user id")
            password = st.text_input (label="Password", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))


with headerSection:
    st.title("Online Movie Ticket Booking Management System")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:    
            show_main_page()  
        else:
            show_login_page()

