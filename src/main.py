import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/DE-2021-11-20.csv")
    print(df.describe())
