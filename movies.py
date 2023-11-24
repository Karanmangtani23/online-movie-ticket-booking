import streamlit as st
import pandas as pd
from database import add_movie
from database import get_movie
from database import del_movie
from database import update_movie
from database import values
def movies():
    st.subheader("Add New Movies:")
    
    col1,col2=st.columns(2)

    with col1:
        movieID=st.text_input('Movie ID:')
        movie_name = st.text_input('Movie Name:')
        movie_length = st.text_input('Duration:')

    with col2:
        language = st.selectbox('Language', ['English', 'Hindi', 'Kannada','Tamil','Telugu','Malayalam'])
        show_start = st.date_input('Select Premier Date')
        show_end = st.date_input('Select Last Showing Date')

    if st.button('Add Movie'):
        add_movie(movieID,movie_name,movie_length,language,show_start,show_end)
        st.success(f'Successfully added Movie: {movie_name}')

    st.subheader("Delete Movie")
    movie_name = st.selectbox("Movies:",options= get_movie(),key=1000)
    if st.button("Delete Movie"):
        del_movie(movie_name)
        st.success(f'Successfully deleted Movie: {movie_name}')
    
    st.subheader("Alter Movie details")
    col1,col2=st.columns(2)

    with col1:
        movie_name = st.selectbox("Movies:",options= get_movie())
        movieID=st.text_input('Movie ID:',key=1340)
        movie_length = st.text_input('Duration:',key=1430)

    with col2:
        language = st.selectbox('Language', ['English', 'Hindi', 'Kannada','Tamil','Telugu','Malayalam'],key=2130)
        show_start = st.date_input('Select Premier Date',key=3120)
        show_end = st.date_input('Select Last Showing Date',key=4120)

    if st.button('Add Movie',key=5130):
        update_movie(movieID,movie_name,movie_length,language,show_start,show_end)
        st.success(f'Successfully updated Movie: {movie_name}')

    if st.button('Show table'):
        data = values('pes1ug21cs268_289_movies')
        df = pd.DataFrame(data)
        st.dataframe(df)