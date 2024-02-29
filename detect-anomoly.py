from tqdm.notebook import tqdm
import pandas as pd
from sqlalchemy import create_engine
import os
import datetime

def rsrq_rule(dB):
    return 0 if not dB else 4 if dB >= -10 else 3 if dB >= -15 else 2 if dB >= -20 else 1
 
def rsrp_rule(dBm):
    return 0 if not dBm else 4 if dBm >= -80 else 3 if dBm >= -90 else 2 if dBm >= -110 else 1


def summery(param, threshold):
    good = len(df[df[param] >= threshold])
    bad = len(df[df[param] < threshold])
    print(f"\nSummery for {param}")
    print("Good: " + str(good) + " | Bad: " + str(bad))
    print(f"Good Percentage: {(good / (good + bad) * 100).__round__(2)}%")

# engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
tqdm.pandas()

if __name__ == '__main__':

    df = pd.read_csv('dump.csv')
    df = df[['rsrp0', 'rsrq']]

    df['rsrp0_score'] = df['rsrp0'].apply(lambda x: rsrp_rule(float(x)) / 4.0 * 100)  
    df['rsrq_score'] = df['rsrq'].apply(lambda x: rsrq_rule(float(x)) / 4.0 * 100)  
    df['quality_score'] = df['rsrp0_score'].apply(lambda x: x * 0.70) + df['rsrq_score'].apply(lambda x: x * 0.30)

    rp = summery("rsrp0_score", 50)
    rq = summery("rsrq_score", 50)
    q = summery("quality_score", 50)
    print(df)
    # df.to_sql('stats', con=engine, if_exists='append', index=False)

    # os.system(f'mv dump.csv dump-x.csv')