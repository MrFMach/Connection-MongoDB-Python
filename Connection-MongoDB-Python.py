#importar classe MongoClient da biblioteca pymongo
from pymongo import MongoClient
cliente = MongoClient()

#imprimir o endereço do host
print(cliente)
