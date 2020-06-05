#importar classe MongoClient da biblioteca pymongo
from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

#criando banco 'meubanco' no mongodb e atribuindo à variável local banco
banco = cliente ['meubanco']
#criando coleção 'meuscursos' no mongodb e atribuindo à variável local cursos
cursos = banco ['meuscursos']
#criando um documento chamado curso
curso = {
    'autor':'Maria',
    'curso':'MongoDB',
    'valor':120,
    'classificação':5
}
#inserindo o documento curso na coleção meuscursos
resultado = cursos.insert_one(curso)

if resultado.acknowledged:
    print('Curso inserido com sucesso. O ID do documento é ' + str(resultado.inserted_id))



