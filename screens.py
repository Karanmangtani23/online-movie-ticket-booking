import streamlit as st
import pandas as pd
import database as db
def screens():
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Add Screens")
        screen_id = st.text_input("Screen-Id:")
        class_s = st.text_input("Class:")
        capacity = st.text_input("No_of_seats:")
        ans = st.button("Add Screen")
        if ans:
            db.add_screen(screen_id,class_s,capacity)
    with col2:
        details = db.view_screenid()
        st.subheader("Update Screen")
        screen_id = st.selectbox("Screen-Id:",options=details)
        class_s = st.text_input("Class:",key=100)
        capacity = st.text_input("No_of_seats:",key=00)
        ans = st.button("Update Screen",key=310)
        if ans:
            db.update_screenid(screen_id,class_s,capacity)
    
    st.subheader("Delete Screen:")
    screen_id = st.selectbox("Screen-Id:",options= db.view_screenid(),key=105)
    if st.button("Delete",key=9905):
        db.del_screenid(screen_id)
        st.success(f'Successfully deleted Price_list: {screen_id}')
    
    if st.button('Show table',key=121212):
        data = db.values('pes1ug21cs268_289_screens')
        df = pd.DataFrame(data)
        st.dataframe(df)