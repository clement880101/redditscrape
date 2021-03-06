import pandas as pd
from sklearn.preprocessing import StandardScaler


def main():
    df = pd.read_csv("redditinterest.csv", index_col=0)
    df = df.loc[:, (df != 0).any(axis=0)]
    print(df)
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    print(df)


if __name__ == "__main__":
    main()
