import pandas as pd

def main():
    nasdaq = pd.read_csv("nasdaq.csv")
    nyse = pd.read_csv("nyse.csv")

    nasdaq = nasdaq.iloc[:, 0]
    nyse = nyse.iloc[:, 0]

    nasdaq.append(nyse, ignore_index=True)
    nasdaq.to_csv("ticker.csv", index=False, header=False)

if __name__ == "__main__":
    main()
