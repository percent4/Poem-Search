import pandas as pd
from pymongo import MongoClient

# 连接MongoDB
conn = MongoClient('mongodb://localhost:27017/')
db = conn["test"]

# 插入诗歌
df = pd.read_csv('poem.csv')
columns = ['title', 'dynasty', 'poet', 'content']
for i in range(df.shape[0]):
    print(i)
    row = df.iloc[i, :]
    db.poem.insert(dict(zip(columns, row[columns])))