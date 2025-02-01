import praw
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter

# Initialize Reddit API client (replace with your credentials)
reddit = praw.Reddit(client_id='TaTUgpWKmFNdqt2CJpHIlg',
                     client_secret='UPoheGVyTyqYSzVdS6xd4qqo10GixQ',
                        user_agent='Reddit Data Analysis')

# Function to fetch top posts from a subreddit
def fetch_top_posts(subreddit="formula1", limit=50):
    posts = []
    for post in reddit.subreddit(subreddit).top(limit=limit):
        posts.append(post.title)
    return posts

# Function to analyze sentiment
def analyze_sentiment(post):
    polarity = TextBlob(post).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Fetch posts and perform sentiment analysis
subreddit_name = "formula1"  # Change this to any subreddit you want
reddit_posts = fetch_top_posts(subreddit_name)
sentiments = [analyze_sentiment(post) for post in reddit_posts]

# Count sentiment categories
sentiment_counts = Counter(sentiments)

# Plot sentiment distribution
plt.figure(figsize=(7, 7))
plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), autopct="%1.1f%%", colors=["green", "gray", "red"])
plt.title(f"Sentiment Analysis of Top Posts in r/{subreddit_name}")
plt.show()
