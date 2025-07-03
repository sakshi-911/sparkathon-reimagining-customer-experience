import pandas as pd 
from sentiment_analyzer import classify_sentiment

def processs_reviews(file):
    df=pd.read_csv(file)
    df['Sentiment']=df['review_text'].apply(classify_sentiment)
    return df

