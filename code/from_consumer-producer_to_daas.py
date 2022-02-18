import pandas as pd
import requests, argparse
import os, json
import numpy as np
import math

data = pd.read_csv('./data/covid19_wordwide_data.csv')
data = data.replace(np.nan, 'NaN')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_address', type=str, default='http://127.0.0.1:5000/')
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--method', type=str, default='ingest')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    n_batch = math.ceil(len(data) / args.batch_size)
    
    # batch ingesting
    if args.method == 'ingest':
        for i_batch in range(n_batch):
            batch_start = i_batch*args.batch_size
            batch_end = min((i_batch+1)*args.batch_size, len(data))
            ingested_rows = range(batch_start, batch_end)
            ingested_dict = data.loc[ingested_rows,:].to_dict(orient='records')
            request = requests.post(args.server_address+'ingestion', json=ingested_dict)
            print('Request status:', request.reason)  

    # clear table
    elif args.method == 'clear':
        request = requests.post(args.server_address+'clear', json={})
        print('Request status:', request.reason)

        