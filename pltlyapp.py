# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:58:38 2022

@author: mjaf8
"""

!pip install pyplot
import pandas as pd
import plotly.express as px


import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import streamlit as st

df=pd.read_csv('C:/Users/mjaf8/Downloads/StudentsPerformance.csv')




mathfig= px.box(y=df['math score'], title = 'Math score',animation_group=df['gender'],color=df['gender'])
readfig=px.box(y=df['reading score'],title = 'Reading score',animation_group=df['gender'],color=df['gender'])
writefig=px.box(y=df['writing score'],title = 'Writing score',animation_group=df['gender'],color=df['gender'])

st.title("Marian Abou Fares - Students' Performances")


st.header("The Data")

st.dataframe(df)
def convert_df(df):
    
    return df.to_csv().encode('utf-8')

csvdf = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csvdf,
   
)
st.header("Students' Distributions")
tab1, tab2, tab3 = st.tabs(["Gender", "Parental Educational Level", "Test Preparation Course"])

with tab1:
   st.header("Gender")
   figg = px.pie(df,"gender",
             color_discrete_sequence = px.colors.sequential.Sunset,
             title = "Gender distribution",
             hole = 0.8)
   st.plotly_chart(figg,use_container_width=False, sharing="streamlit")
   
with tab2:
   st.header("Parental Educational Level")
   figg2 = px.pie(df,"parental level of education",
             color_discrete_sequence = px.colors.sequential.Sunset,
             title = "Parental Educational Level distribution",
             hole = 0.8)
   st.plotly_chart(figg2,use_container_width=False, sharing="streamlit")
   
with tab3:
    st.header("Test Preparation Course")
    figg2 = px.pie(df,"test preparation course",
              color_discrete_sequence = px.colors.sequential.Sunset,
              title = "Test Preparation Course",
              hole = 0.8)
    st.plotly_chart(figg2,use_container_width=False, sharing="streamlit")
    
   
   
st.header("Choose the Score you want to view")
option=st.selectbox("Score", ("None",'Math Scores', 'Reading Scores', 'Writing Scores'))


if option==("Math Scores"):
   
    st.subheader("Math Scores")
    if st.checkbox("Summary of the scores"):
        st.plotly_chart(mathfig, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("Males tend to do better in math than females.")
    elif st.checkbox("Race/Ethnicity effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["math score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist= px.histogram(filtered_data, x="race/ethnicity",  title='Math Score - Race', barmode='overlay')
        st.plotly_chart(hist, use_container_width=False, sharing="streamlit")
    elif st.checkbox("Lunch effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["math score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist2=px.histogram(filtered_data,x="lunch",title='Math Score - Lunch', barmode='overlay')
        st.plotly_chart(hist2, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("""The graphs imply that the way the lunch is chosen has a big impact on the students’score. It can be observed that the number of students who chose the standard lunch had a higher score than the free/reduced lunch option.""")   



if option==("Reading Scores"):
    st.subheader("Reading Scores")
    if st.checkbox("Summary of the scores"):
        st.plotly_chart(readfig, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("Females tend to do better in reading than males.")
    elif st.checkbox("Race/Ethnicity effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["reading score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist= px.histogram(filtered_data, x="race/ethnicity",  title='Reading Score - Race', barmode='overlay')
        st.plotly_chart(hist, use_container_width=False, sharing="streamlit")
    elif st.checkbox("Lunch effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["reading score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist2=px.histogram(filtered_data,x="lunch",title='Reading Score - Lunch', barmode='overlay')
        st.plotly_chart(hist2, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("""The graphs imply that the way the lunch is chosen has a big impact on the students’score. It can be observed that the number of students who chose the standard lunch had a higher score than the free/reduced lunch option.""")   
if option==("Writing Scores"):
    st.subheader("Writing Scores")
    if st.checkbox("Summary of the scores"):
        st.plotly_chart(writefig, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("Females tend to do better in writing than males.")
    elif st.checkbox("Race/Ethnicity effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["writing score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist= px.histogram(filtered_data, x="race/ethnicity",  title='Writing Score - Race', barmode='overlay')
        st.plotly_chart(hist, use_container_width=False, sharing="streamlit")
    elif st.checkbox("Lunch effect on scores"):
        filtering = st.slider('Choose the grade', 0, 100, 67)
        filtered_data = df[df["writing score"] == filtering]
        st.subheader(f'Grade {filtering}/100')
        hist2=px.histogram(filtered_data,x="lunch",title='Writing Score - Lunch', barmode='overlay')
        st.plotly_chart(hist2, use_container_width=False, sharing="streamlit")
        with st.expander("See Analysis"):
            st.write("""The graphs imply that the way the lunch is chosen has a big impact on the students’score. It can be observed that the number of students who chose the standard lunch had a higher score than the free/reduced lunch option.""")            
        

    
    
st.subheader("Relation between the different scores")
fig = sns.pairplot(df[["math score", "reading score", "writing score", "gender"]], hue="gender", height=4);

st.pyplot(fig)
with st.expander("See Analysis"):
    st.write("""The plots show that there is a high correlation between scores, especially reading and writing.

        
    """)


# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'
