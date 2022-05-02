import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:NASA, OR from:YahooFinance) until:2022-04-16 since:2021-01-01"
limit = 5000
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content,tweet.likeCount])

df = pd.DataFrame(tweets,columns=["Date", "Username", "Tweet", "LikeCount"])
print(df)

df.to_csv("nasa_yahoofinance.csv")