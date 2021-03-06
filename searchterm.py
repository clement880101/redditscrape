import pandas as pd
import datetime as dt
import praw
import time


def main():
    # If you want to enter own search term, use this:
    # search_term = ["pwc"]
    # category = ["consulting"]

    # Reads input from compiled ticker list.
    search_term = pd.read_csv("ticker.csv").values.flatten().tolist()
    category = ["stock"] * len(search_term)
    period = 300
    time_filter="year"
    output = "redditinterest2.csv"

    client_id = 'lql9yxsiL66vew'
    client_secret = 'O41A6Bu5IySyhtw7hzWyfFjGniCV0Q'
    user_agent = 'redditscrape'
    start = time.time()
    savetime = start

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    targetdate = dt.datetime.utcnow().date()
    data = pd.DataFrame(pd.date_range(end=targetdate, periods=period), columns=["date"])
    data = data.iloc[::-1].reset_index(drop=True)

    if len(category) != len(search_term):
        return -1

    for z in range(len(search_term)):
        # Instead of /all, this search is more comprehensive
        print("Category: " + category[z])
        print("Search Term: " + search_term[z])
        subreddit = reddit.subreddits.search(category[z])

        temp = [0] * period
        for subred in subreddit:
            feed = subred.search(search_term[z], sort="new", time_filter=time_filter)
            for post in feed:
                postdate = dt.datetime.fromtimestamp(post.created_utc).date()

                # TODO Change to mergesort to boost speed
                for i in range(len(temp)):
                    if postdate == (targetdate - dt.timedelta(i)):
                        temp[i] = temp[i] + 1
                        break
        temp = pd.Series(temp, name=search_term[z])
        data = pd.concat((data, temp), axis=1)

        print("Total Runtime: " + str(dt.timedelta(seconds=time.time() - start)))
        print("Time Since Save: " + str(dt.timedelta(seconds=time.time() - savetime)))
        if time.time() - savetime >= 600:
            data.to_csv(output, index=False)
            savetime = time.time()
        print("-----------------")

    data.to_csv(output, index=False)


if __name__ == "__main__":
    main()
