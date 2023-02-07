import tweepy
import pandas as pd

# Authenticate to Twitter API
auth = tweepy.OAuthHandler("API_key", "API_private_key")
auth.set_access_token("Token_key", "Token_private_key")


# Create API object
api = tweepy.API(auth)

# Define the date range to search for new users
start_date = "2022-01-01"
end_date = "2022-12-31"

# Define a list to store the users' data
users_data = []

# Loop through all tweets in the date range
for tweet in tweepy.Cursor(api.search_tweets, q="from:username", since_id=start_date, until=end_date).items():
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
