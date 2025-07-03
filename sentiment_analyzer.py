from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()

def classify_sentiment(text):
    score=analyzer.polarity_scores(text)["compound"]
    if score<-0.05: return "Negative"
    elif score>=0.05: return "Positive"
    else: return "Neutral"