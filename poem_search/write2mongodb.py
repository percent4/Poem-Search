import pandas as pd
from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/')
db = conn["test"]

df = pd.read_csv('poem.csv')
columns = ['title', 'dynasty', 'poet', 'content']
for i in range(df.shape[0]):
    print(i)
    row = df.iloc[i, :]
    db.poem.insert(dict(zip(columns, row[columns])))