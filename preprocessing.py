import pandas as pd
from sklearn.preprocessing import StandardScaler


def main():
    dataframe = pd.read_csv("redditinterest.csv", index_col=0)
    scalar = StandardScaler()
    dataframe = scalar.fit_transform(dataframe)
    print(dataframe)


if __name__ == "__main__":
    main()