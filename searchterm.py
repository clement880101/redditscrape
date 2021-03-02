import pandas as pd
import praw

def main():
    search_term = "gme"

    client_id = 'lql9yxsiL66vew'
    client_secret = ''
    user_agent = 'redditscrape'
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    list = reddit.subreddit("all").search(search_term, time_filter=)

    for submission in list:
        print(submission.title)


if __name__ == "__main__":
    main()