import streamlit as st
import database as db
import pandas as pd

def prices():
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Add Price_list")
        price_id = st.text_input("Price-Id:")
        Type = st.text_input("Type:")
        day = st.text_input("Day:")
        price = st.text_input("Price:")
        ans = st.button("Add Price_list")
        if ans:
            db.add_price(price_id,Type,day,price)
    with col2:
        details = db.view_price_list()
        st.subheader("Update Price_list")
        ids = []
        for x in details:
            ids.append(x[0])
        price_id = st.selectbox("Price-Id:",options=ids,key=123)
        Type = st.text_input("Type:",key=124)
        day = st.text_input("Day:",key=134)
        price = st.text_input("Price:",key=314)
        ans = st.button("Update Price_list",key=312)
        if ans:
            db.update_price(price_id,Type,day,price)
    
    st.subheader("Delete Price_list:")
    price_id = st.selectbox("Price-id:",options= db.view_priceid(),key=101)
    if st.button("Delete",key=9901):
        db.del_priceid(price_id)
        st.success(f'Successfully deleted Price_list: {price_id}')

    if st.button('Show table',key=12121):
        data = db.values('pes1ug21cs268_289_price_list')
        df = pd.DataFrame(data)
        st.dataframe(df)