import pymongo, argparse
import pandas as pd
import math
import time
from threading import Thread

client = pymongo.MongoClient('mongodb+srv://phihd:iXkIXCNJhQNQriwF@cluster0.vwz1m.mongodb.net/bdp-a1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
database = client['bdp-a1']

# 3 collections to simulate 3 shards
covid_tables = [database['covid19'], database['covid19_1'], database['covid19_2']]

data = pd.read_csv('../data/covid19_wordwide_data.csv')


class IngestWorker(Thread):
    def __init__(self, args, record_end_time):
        Thread.__init__(self)
        self.n_concurrence = args.n_concurrence
        self.record_end_time = record_end_time
        self.n_shards = args.n_shards

    def run(self):
        # Hashed sharding
        for i, covid_table in enumerate(covid_tables):
            ingested_rows = range(i%self.n_shards, len(data), self.n_shards)
            ingested_dict = data.loc[ingested_rows,:].to_dict(orient='records')
            covid_table.insert_many(ingested_dict)

        if self.record_end_time:
            print(f'{args.n_concurrence} concurrent ingestions take {time.time()-start_time} seconds.')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_concurrence', type=int, default=1)
    parser.add_argument('--record', type=bool, default=False)
    parser.add_argument('--n_shards', type=int, default=3)
    return parser.parse_args()



if __name__ == "__main__":
    args = parse_args()
    start_time = time.time()
    for i in range(args.n_concurrence):
        thread = IngestWorker(args, record_end_time=(i==args.n_concurrence-1))
        thread.start()

        

