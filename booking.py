import streamlit as st
import database as d
import pandas as pd
def booking():
    st.subheader("Booking details")
    input = str(st.date_input("Select Date"))
    output = d.view(input)
    df = pd.DataFrame(output,columns=['Show_id','Ticket_id','Seat_no','Type','Time','Date','Screen_id','Movie_id','Price_id'])
    if(len(df)!=0):
        st.dataframe(df)
    else:
        st.write("No bookings!!!")