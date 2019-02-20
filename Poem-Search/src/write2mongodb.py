import pandas as pd
from pymongo import MongoClient

class Write2MongoDB(object):

    def __init__(self, file):
        self.file = file

    def write(self):

        try:
            # 连接MongoDB
            conn = MongoClient(host="mongo", port=27017)
            db = conn["test"]

            # 插入诗歌
            df = pd.read_csv(self.file)
            print('Write data in %s to mongodb, please wait...' % self.file)
            columns = ['title', 'dynasty', 'poet', 'content']
            for i in range(df.shape[0]):
                # print(i)
                row = df.iloc[i, :]
                db.poem.insert(dict(zip(columns, row[columns])))
            print("Write to mongodb successfully! You can visit the website: localhost:8000/query .")
        except Exception as err:
            print('error:\n')
            print(err)