import pandas as pd
import requests, argparse
import os, json
import numpy as np
import math

data = pd.read_csv('../data/covid19_wordwide_data.csv')
data = data.replace(np.nan, 'NaN')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_address', type=str, default='http://127.0.0.1:5000/')
    parser.add_argument('--method', type=str, default='ingest')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    # batch ingesting
    if args.method == 'ingest':
        ingested_dict = data.loc[data.index,:].to_dict(orient='records')
        request = requests.post(args.server_address+'ingestion', json=ingested_dict)
        print('Request status:', request.reason)  

    # clear table
    elif args.method == 'clear':
        request = requests.post(args.server_address+'clear', json={})
        print('Request status:', request.reason)

        