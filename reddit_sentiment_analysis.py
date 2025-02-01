import praw
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter


reddit = praw.Reddit(client_id='',
                     client_secret='',
                        user_agent='Reddit Data Analysis')


def fetch_top_posts(subreddit="formula1", limit=50):
    posts = []
    for post in reddit.subreddit(subreddit).top(limit=limit):
        posts.append(post.title)
    return posts


def analyze_sentiment(post):
    polarity = TextBlob(post).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


subreddit_name = "formula1"  
reddit_posts = fetch_top_posts(subreddit_name)
sentiments = [analyze_sentiment(post) for post in reddit_posts]


sentiment_counts = Counter(sentiments)


plt.figure(figsize=(7, 7))
plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct="%1.1f%%", colors=["green", "gray", "red"])
plt.title(f"Sentiment Analysis of Top Posts in r/{subreddit_name}")
plt.show()
