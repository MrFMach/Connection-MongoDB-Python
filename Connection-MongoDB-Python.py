#importar classe MongoClient da biblioteca pymongo
from pymongo import MongoClient
import pprint

cliente = MongoClient('mongodb://localhost:27017')

#criando banco 'meubanco' no mongodb e atribuindo à variável local banco
banco = cliente ['meubanco']
#criando coleção 'meuscursos' no mongodb e atribuindo à variável local cursos
cursos = banco ['meuscursos']
#inserindo vários documentos em forma de matriz

matriz_cursos = [
    {
        'autor': 'Higor',
        'curso': 'Linguagem C',
        'valor': 290,
        'classificação': 4
    },  {
        'autor': 'Teo',
        'curso': 'POO',
        'valor': 79,
        'classificação': 3
    },
]

#inserindo a matriz na coleção e imprimindo mensagem dos cursos inseridos
resultado = cursos.insert_many(matriz_cursos)
for objeto_id in resultado.inserted_ids:
    print('Curso inserido com sucesso. O ID do curso é: ' + str(objeto_id))

#encontrando resultados específicos, ordenados e limitados
resultado = cursos.find().sort([('autor', 1), ('valor', -1)]).limit(3)
#imprimindo resultados utilizando pprint (várias linhas)
for res in resultado:
    pprint.pprint(res)

#Update
cursos.update_one({
    'curso': 'MongoDB'
}, {
   '$set': {
       'curso': 'MongoDB - Fundamentos'
   } 
})