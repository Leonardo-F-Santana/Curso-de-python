#É uma coleção ordenada e mutavel
#Lista é multi tipos de valores, ela pode conter valores duplicados, são caracterizados por iniciar com parenteses, são ordenados
lista = ["Carro", True, 2, 3.5, 2]
print(lista)
print(type(lista))
print("-"*30)

#É uma coleção ordenada e imutavel
#Tupla é multi tipos de valores, ela pode conter valores duplicados, são caracterizados por iniciar com colchetes, são ordenados
tupla = ("Carro", True, 2 , 3.5)
print(tupla)
print(type(tupla))
print("-"*30)


#É uma coleção ordenada e imutavel e não permite nenhum membro duplicado
# O dicionario sempre tem sua Chave: Valor, são iniciadas com chaves e são multi tipos de valores
dicionario = {"Nome": "carro", "Logica": True, "numero": "2", "outroNumero": "3.5"}
print(dicionario)
print(type(dicionario))
print("-"*30)

#É uma coleção desordenada e imutavel
# Conjuntos não possuem ordem e não podem ter o mesmo elemento repetido, são iniciadas por chaves
conjunto = {"Carro", True, 2 , 3.5}
print(conjunto)
print(type(conjunto))
print("-"*30)