import streamlit as st
import pandas as pd
import plotly.express as px
from utils import processs_reviews

st.set_page_config(page_title="Reimagining Customer Experience",layout='wide')

st.title("Your Customers Are Talking. Are You Listening?")

uploaded_file=st.file_uploader("Upload your customer feedback CSV",type=["csv"])
if uploaded_file:
    df=processs_reviews(uploaded_file)
    st.success("Sentiment Analysis Complete")

    st.subheader("Semtiment Distribution")
    pie_fig=px.pie(df, names="Sentiment",title="Overall Sentiment Distribution")
    st.plotly_chart(pie_fig,use_container_width=True)

    st.subheader("Sentiment Over Time")
    df['date']= pd.to_datetime(df['date'])
    time_data=df.groupby([df['date'],'Sentiment']).size().reset_index(name='count')
    line_fig=px.line(time_data,x='date',y='count',color='Sentiment',title='Daily Sentiment Trends')
    st.plotly_chart(line_fig,use_container_width=True)


    st.subheader("Top Negative Feedback")
    negative_df=df[df['Sentiment']=='Negative'].head(5)

    st.table(negative_df[['review_text','date']])

    st.download_button(label="Download Results",data=df.to_csv(index=False),file_name='processed_sentiment.csv',mime='text/csv')

    