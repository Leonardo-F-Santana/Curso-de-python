import dataset

# Conectar ao banco de dados (em memória ou persistente)
db = dataset.connect('sqlite:///:memory:')
table = db['usuario']

# Funções CRUD
def criar(nome, idade, genero=None):
    registro = dict(name=nome, age=idade, gender=genero)
    table.insert(registro)
    print(f"Usuário {nome} criado com sucesso!")

def ler():
    for usuario in table.all():
        print(usuario)

def atualizar(id_usuario, novos_dados):
    table.update(dict(id=id_usuario, **novos_dados), ['id'])
    print(f"Usuário com ID {id_usuario} atualizado!")

def deletar(id_usuario):
    table.delete(id=id_usuario)
    print(f"Usuário com ID {id_usuario} deletado!")

# Exemplo de uso
criar('Leonardo', 38)
criar('Savana', 43, genero='female')
ler()  # Listar todos os usuários

Leonardo = table.find_one(name='Leonardo')  # Encontrar John
print("Leonardo encontrado:", Leonardo)

atualizar(Leonardo['id'], {'name': 'Leonardo', 'age': 38})  # Atualizar John
ler()

deletar(Leonardo['id'])  # Deletar John
ler()