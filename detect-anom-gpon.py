from tqdm.notebook import tqdm
import pandas as pd
from sqlalchemy import create_engine
import os
import datetime


def rx_rule(dB):
    return -1 if not dB else 1 if dB <= -30 else 0


def tx_rule(dB):
    return -1 if not dB else 1 if dB <= -30 else 0


def summery(param, threshold):
    good = len(df[df[param] >= threshold])
    bad = len(df[df[param] < threshold])
    print(f"\nSummery for {param}")
    print("Good: " + str(good) + " | Bad: " + str(bad))
    print(f"Good Percentage: {(good / (good + bad) * 100).__round__(2)}%")


engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
tqdm.pandas()

if __name__ == "__main__":

    df = pd.read_csv("dump.csv")
    df = df[["rxpower_db", "txpower_db"]]

    df.rename(columns={"rxpower_db": "rx", "txpower_db": "tx"}, inplace=True)

    df["rx_score"] = df["rxpower_db"].apply(lambda x: rx_rule(float(x)) / 4.0 * 100)
    df["tx_score"] = df["txpower_db"].apply(lambda x: tx_rule(float(x)) / 4.0 * 100)
    df["quality_score"] = df["rx_score"].apply(lambda x: x * 0.70) + df[
        "tx_score"
    ].apply(lambda x: x * 0.30)


    rp = summery("rsrp0_score", 50)
    rq = summery("rsrq_score", 50)
    q = summery("quality_score", 50)
    print(df)

    # id serial primary key,
    # rx FLOAT,
    # tx FLOAT,
    # ymd TIMESTAMP,
    # rx_score FLOAT,
    # tx_score FLOAT,
    # anomoly BOOLEAN,
    # user VARCHAR(11)

    df.to_sql("stats", con=engine, if_exists="append", index=False)

    # os.system(f'mv dump.csv dump-x.csv')
