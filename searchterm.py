import pandas as pd
import datetime as dt
import praw


def main():
    search_term = ["gme", "amc", "tlry", "acb"]
    category = ["stock", "stock", "stock", "stock"]
    period = 100

    client_id = 'lql9yxsiL66vew'
    client_secret = ''
    user_agent = 'redditscrape'

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
        print("*********")
        subreddit = reddit.subreddits.search(category[z])

        temp = [0] * period
        for subred in subreddit:
            print("Subreddit: ", subred.display_name)
            feed = subred.search(search_term[z], sort="new", time_filter="year")
            for post in feed:
                postdate = dt.datetime.fromtimestamp(post.created_utc).date()
                for i in range(len(temp)):
                    pp = targetdate - dt.timedelta(i)
                    if postdate == pp:
                        temp[i] = temp[i] + 1
                        break
        temp = pd.Series(temp, name=search_term[z])
        data = pd.concat((data, temp), axis=1)
        print("-----------------")

    name = search_term[0] + "-" + category[0] + ".csv"
    data.to_csv(name, index=False)


if __name__ == "__main__":
    main()
