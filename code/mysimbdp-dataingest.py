import pymongo, argparse
import pandas as pd
import math
import time
from threading import Thread

client = pymongo.MongoClient('mongodb+srv://phihd:iXkIXCNJhQNQriwF@cluster0.vwz1m.mongodb.net/bdp-a1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
database = client['bdp-a1']
covid_table = database['covid19']
data = pd.read_csv('./data/covid19_wordwide_data.csv')


class IngestWorker(Thread):
    def __init__(self, args, record_end_time):
        Thread.__init__(self)
        self.batch_size = args.batch_size
        self.n_concurrence = args.n_concurrence
        self.record_end_time = record_end_time

    def run(self):
        for i_batch in range(n_batch):
            batch_start = i_batch*self.batch_size
            batch_end = min((i_batch+1)*self.batch_size, len(data))
            ingested_rows = range(batch_start, batch_end)
            ingested_dict = data.loc[ingested_rows,:].to_dict(orient='records')
            covid_table.insert_many(ingested_dict)
        
        if self.record_end_time:
            print(f'{args.n_concurrence} concurrent ingestion take {time.time()-start_time} seconds.')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--n_concurrence', type=int, default=1)
    parser.add_argument('--record', type=bool, default=False)
    return parser.parse_args()



if __name__ == "__main__":
    args = parse_args()
    n_batch = math.ceil(len(data) / args.batch_size)
    start_time = time.time()
    for i in range(args.n_concurrence):
        thread = IngestWorker(args, record_end_time=(i==args.n_concurrence-1))
        thread.start()

        

