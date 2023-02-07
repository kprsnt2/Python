import tweepy
import pandas as pd
from datetime import datetime, timedelta

# Authenticate to Twitter API
auth = tweepy.OAuthHandler("API_key", "API_private_key")
auth.set_access_token("Token_key", "Token_private_key")
# Create API object
api = tweepy.API(auth)

# Get the current date and the date one year ago
now = datetime.now()
start_date = (now - timedelta(days=365)).strftime("%Y-%m-%d")

# Define a list to store the users' data
users_data = []

# Define the search query
query = "#tag"

# Loop through all tweets containing the query in the last year
for tweet in tweepy.Cursor(api.search_tweets, q=query, since_id=start_date).items():
    # Get the user data from each tweet
    user = tweet.user
    users_data.append({
        "Username": user.screen_name,
        "Name": user.name,
        "Location": user.location,
        "Description": user.description,
        "Followers": user.followers_count,
        "Friends": user.friends_count,
        "Listed": user.listed_count,
        "Statuses": user.statuses_count,
        "Created": user.created_at,
    })

# Convert the users' data to a Pandas DataFrame
df = pd.DataFrame(users_data)

# Save the DataFrame to a CSV file
df.to_csv("users.csv", index=False)
