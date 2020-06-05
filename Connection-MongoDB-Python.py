#importar classe MongoClient da biblioteca pymongo
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

#criando banco 'meu banco' no mongodb e atribuindo à variável banco
banco = cliente ['meubanco']
#criando coleção 'cursos' e atribuindo à variável meuscursos
cursos = banco ['meuscursos']


print(cursos)
