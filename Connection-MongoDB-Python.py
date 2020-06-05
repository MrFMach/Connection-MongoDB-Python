#importar classe MongoClient da biblioteca pymongo
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

#criando banco 'meubanco' no mongodb e atribuindo à variável local banco
banco = cliente ['meubanco']
#criando coleção 'meuscursos' no mongodb e atribuindo à variável local cursos
cursos = banco ['meuscursos']
#inserindo vários documentos
matriz_cursos = [
    {
        'autor': 'José da Silva',
        'curso': 'Python avançado',
        'valor': 130,
        'classificação': 5 
    },  {
        'autor': 'Luan Cardoso',
        'curso': 'Lógica de Programação',
        'valor': 70,
        'classificação': 4 
    },  {
        'autor': 'Rita Nogueira',
        'curso': 'HTML e CSS Básico',
        'valor': 180,
        'classificação': 4 
    },  {
        'autor': 'Mai Tsnuga',
        'curso': 'Algorítmos',
        'valor': 135,
        'classificação': 3 
    },
]

resultado = cursos.insert_many(matriz_cursos)
for objeto_id in resultado.inserted_ids:
    print('Curso inserido com sucesso. O ID do curso é: ' + str(objeto_id))