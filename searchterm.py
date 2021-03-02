import pandas as pd
from datetime import datetime
import praw


def main():
    search_term = "gme"
    category = "stocks"

    client_id = 'lql9yxsiL66vew'
    client_secret = ''
    user_agent = 'redditscrape'

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    # Some subreddits can opt out from /all, therefore we used another way to search
    list = reddit.subreddits.search(category)

    maxutc = (datetime.utcnow().timestamp() // 86400) * 86401
    data = pd.Series(0, index=pd.date_range(end=datetime.today().strftime('%Y-%m-%d'), periods=100),
                     name="occurrences")
    data = data.iloc[::-1]

    for subred in list:
        print("Subreddit: ", subred.display_name)
        feed = subred.search(search_term, sort="new", time_filter="year")
        for post in feed:
            for i in range(len(data)):
                if (post.created_utc <= maxutc - (i * 86400)) and (post.created_utc > maxutc - ((i + 1) * 86400)):
                    data[i] = data[i] + 1
                    break
        print("complete")

    name = search_term + ":" + category + ".csv"
    data.to_csv(name, index=True)


if __name__ == "__main__":
    main()
