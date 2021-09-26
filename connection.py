# Este arquivo faz a conexão com o MongoDB
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.desafio_Carrefour

trends_collection = db.trends