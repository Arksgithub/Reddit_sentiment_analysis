# Reddit Sentiment Analysis on r/formula1

## 📌 Project Overview
This project analyzes the sentiment of top posts from the **r/formula1** subreddit using the **Reddit API (PRAW)** and **TextBlob** for sentiment analysis. The results are visualized in a **pie chart** to show the distribution of positive, negative, and neutral sentiments.

## 🚀 Features
- Fetches **top posts** from r/formula1 using the **Reddit API**.
- Performs **sentiment analysis** using **TextBlob**.
- Visualizes the sentiment distribution using **Matplotlib**.

## 📂 Technologies Used
- **Python** 🐍
- **PRAW (Python Reddit API Wrapper)** 🔗
- **TextBlob (Sentiment Analysis)** 📝
- **Matplotlib (Data Visualization)** 📊

## 📦 Installation & Setup
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install praw textblob matplotlib
```

### 2️⃣ Get Reddit API Credentials
To access Reddit data, you need to create an app on [Reddit's Developer Portal](https://www.reddit.com/prefs/apps):
1. Click **Create an App**.
2. Select **Script**.
3. Copy your `client_id`, `client_secret`, and `user_agent`.

### 3️⃣ Configure API Credentials
Replace `your_client_id`, `your_client_secret`, and `your_user_agent` in `reddit_sentiment.py`:
```python
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="your_user_agent"
)
```

## 🛠 How to Run
```sh
python reddit_sentiment.py
```

## 📊 Example Output
After running the script, a **pie chart** is generated showing the sentiment distribution:
- 🟢 **Positive**
- ⚪ **Neutral**
- 🔴 **Negative**



