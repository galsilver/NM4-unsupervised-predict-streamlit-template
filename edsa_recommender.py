"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    # Creates a main title and subheader on your page -
    # these are static across all pages
    # Creating sidebar with selection box -
    st.sidebar.image("log.jpeg", width =150)
    st.sidebar.title("Movie Recommender BOT®")
    st.sidebar.title("Menu")  
    page_options = ["Meet the Team","Information","EDA","Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option",page_options)
    
    # Building the Meet the Team page
    if page_selection =="Meet the Team":
        # Header contents
        #st.image("Frank.jpeg", caption="Director", width=200)
        #Display Images side by side        
        from PIL import Image        
        col1, col2 = st.columns(2)
        with col1:
            st.header("Muhammad Yahya")
            st.subheader("President")             
            st.image('Yahya.jpeg', width =300)
        with col2:
            st.header("Rachael Njuguna")
            st.subheader("Vice-President")             
            st.image('Recheal.jpeg', width =360)                                   
        col3, col4 = st.columns(2)        
        with col3:
            st.header("Francis Ikegwu")
            st.subheader("Cloud expert")            
            st.image('Frank.jpeg', width=300)            
        with col4:
            st.header("Taiwo Aremu")
            st.subheader("Director Strategies ")             
            st.image('Taiwo.jpeg', width =300)                      
        col5, col6 = st.columns(2)             
        with col5:
            st.header("Molapo kgarose")
            st.subheader("Technical Operations")             
            st.image('Molapo.jpeg', width =300)                         
                
        st.subheader("More information")
        if st.checkbox('Show contact information'): # data is hidden if box is unchecked
            st.info("francisikegwu@yahoo.com, yahyaolalekan@gmail.com, molapokgarose@gmail.com, taiwo.it@gmail.com,  rachaelnjuguna418@gmail.com") 
        #with st.expander("Expand to see Company's video profile"):       
            #video_file = open('Video.mp4', 'rb')
            #video_bytes = video_file.read()
            #st.video(video_bytes)            
        #st.sidebar.subheader("Defining growth through data")            
            #st.success("Text Categorized as: {}".format(prediction))
    
    # Building the Recommender System page
    if page_selection == "Recommender System":
        # Header contents
        #st.image("Frank.jpeg", caption="Director", width=200)
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    # Building out the EDA page
    if page_selection == "EDA":
        st.title("Exploratory Data Analysis")
        st.subheader("EDA Chart")  
        #st.image('EDA_pix.jpg')
        st.subheader("Graph representation of the models used")        
        #st.image('model_chart.jpg')        
        st.subheader("Additional EDA Graph")
        #st.image('EDA_Graph.jpg')   
        
        
    # Building out the "Information" page
    if page_selection == "Information":
        st.title("Information Page")
        st.subheader("Mission Statement")
        st.info("To Provide an accurate and robust movie recommender BOT to companies, more mission statements will be added.")
        st.subheader("Vision Statement")
        st.info("A model that is able to recommend movies to client based on their previous views.")      
        st.subheader("Will display model comparisms and how we pick the best model")
        #st.image('model.jpg')
        st.subheader("Charts that will be gotten from our presentation")
        #st.image("charts.jpg")
        st.subheader("Additional charts if need be")
        #if st.checkbox('Show raw data'): # data is hidden if box is unchecked
            #st.write(raw[['A', 'B']]) # will write the df to the page
        
       
    
    

if __name__ == '__main__':
    main()
