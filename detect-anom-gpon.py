from tqdm.notebook import tqdm
import pandas as pd
from sqlalchemy import VARCHAR, Boolean, Column, Float, Integer, MetaData, String, Table, create_engine, select
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

    df = pd.read_csv("tmp.csv")
    print(df.columns)
    df = df[["rxpower_db", "txpower_db", "pppusername", "ymd"]]

    df.rename(columns={"rxpower_db": "rx", "txpower_db": "tx", "pppusername": "telnum"}, inplace=True)

    df["rx_score"] = df["rx"].apply(lambda x: rx_rule(float(x)))
    df["tx_score"] = df["tx"].apply(lambda x: tx_rule(float(x)))
    df["anomoly"] = df["rx_score"] + df["tx_score"]

    print(df.columns)

    # id serial primary key,
    # rx FLOAT,
    # tx FLOAT,
    # ymd TIMESTAMP,
    # rx_score FLOAT,
    # tx_score FLOAT,
    # anomoly BOOLEAN,
    # user VARCHAR(11)

    metadata_obj = MetaData()
    user_table = Table("data_ont_4", metadata_obj, Column("rx", Float()), Column("tx", Float()), Column("rx_score", Float()), Column("tx_score", Float()), Column("anomoly", Float()), Column("telnum", String(11)),  Column("ymd", String(8)))

    df.to_sql("data_ont_4", con=engine, if_exists="append", index=False)

    stmt = select(user_table)
    print(stmt)

    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)

    # os.system(f'mv dump.csv dump-x.csv')
