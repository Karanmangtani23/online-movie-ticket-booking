import streamlit as st
import pandas as pd
import database 
# from database import del_shows

def shows():
    st.subheader("Add New Shows:")
    col1,col2=st.columns(2)
    
    with col1:
        show_id = st.text_input("Show-Id:")
        Type  = st.text_input("Type")
        time = str(st.time_input("Time"))
        date = st.date_input("Date")
    with col2:
        screen_id = st.selectbox(label = "Screen-Id",options = database.view_screenid())
        movie_id = st.selectbox(label="Movie-Id",options=database.view_movieid())
        price_id = st.selectbox(label="Price-Id",options=database.view_priceid())
        ans = st.button(label="Add")
        if ans:
            database.add_shows(show_id,Type,time,date,screen_id,movie_id,price_id) 

    st.subheader("Update Shows:")
    col1,col2=st.columns(2)
    
    with col1:
        show_id = st.text_input("Show-Id:",key=9)
        Type  = st.text_input("Type",key=99)
        time = str(st.time_input("Time",key=91))
        date = st.date_input("Date",key=92)
    with col2:
        screen_id = st.selectbox(label = "Screen-Id",options = database.view_screenid(),key=93)
        movie_id = st.selectbox(label="Movie-Id",options=database.view_movieid(),key=94)
        price_id = st.selectbox(label="Price-Id",options=database.view_priceid(),key=95)
        ans = st.button(label="Update",key=96)
        if ans:
            database.update_shows(show_id,Type,time,date,screen_id,movie_id,price_id) 

    st.subheader("Delete Shows")
    show_id = st.selectbox("Shows:",options= database.get_show(),key=1001)
    if st.button("Delete Movie",key=991):
        database.del_shows(show_id)
        st.success(f'Successfully deleted Show: {show_id}')

    if st.button('Show table',key=1111):
        data = database.values('pes1ug21cs268_289_shows')
        df = pd.DataFrame(data)
        st.dataframe(df)