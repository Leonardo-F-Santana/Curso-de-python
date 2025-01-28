# class SomaLista:
#     def __init__(self, numeros):
#         self.numeros = numeros
#     def calcular_soma(self):
#         return sum(self.numeros)
# numeros = [6, 7, 8, 9, 10 ]
# soma_lista = SomaLista(numeros)
# print(soma_lista.calcular_soma())

# num = input("Digite o número ") 

# num=num*2 
# print("Digitou o número", num, "com sucesso") 

 
# def fatorial(n): 
#     if n == 0: 
#      return 1 
#     else:
#         return n * fatorial(n - 1) 

# def calcula_resultado(a, b): 
#     return fatorial(a) + b 

# a = 5 
# b = 20 
# resultado = calcula_resultado(a, b) 

# print(resultado) 
# def fatorial(n): 
#     if n == 0:
#         return 1 
#     else: 
#         return n * fatorial(n - 1) 

# def calcula_resultado(a, b): 
#     return fatorial(a) + fatorial(b) 

# a = 4 
# b = 6 
# resultado = calcula_resultado(a, b) 

# print(resultado) 


# x = 10 
# y = "20" 
# z = 2.5 
# lst = [1, 2, 3] 

# resultado = int((x + y) / z + lst[1] * len(y)) + 10.0 

# print(resultado) 

# class Animal: 

#     def __init__(self, nome): 

#         self.nome = nome 

#     def emitir_som(self): 

#         print("Som genérico") 

# class Cachorro(Animal): 

#     def emitir_som(self): 

#         print("Au au") 

# class Gato(Animal): 

#     def emitir_som(self): 

#         print("Miau") 

# animal1 = Animal("Rex") 

# animal2 = Cachorro("Totó") 

# animal3 = Gato("Minhoca") 

 

# animal1.emitir_som() 

# animal2.emitir_som() 

# animal3.emitir_som() 

# num = input('Digite um numero: ')
# num = num*2
# print(f'O numero digitado foi', num)


class ContaBancaria:

def __init__(self, titular, saldo_inicial=0):

self.titular = titular

self.saldo = saldo_inicial

def depositar(self, valor):

if valor > 0:

self.saldo += valor

print(f"Depósito de R${valor:.2f} realizado com sucesso.")

else:

print("O valor do depósito deve ser positivo.")

def sacar(self, valor):

if valor > self.saldo:

print("Saldo insuficiente.")

elif valor > 0:

self.saldo -= valor

print(f"Saque de R${valor:.2f} realizado com sucesso.")

else:

print("O valor do saque deve ser positivo.")

def consultar_saldo(self):

print(f"O saldo atual de {self.titular} é: R${self.saldo:.2f}")

conta1 = ContaBancaria("João", 1000)

conta1.consultar_saldo()

conta1.depositar(500)

conta1.sacar(200)

conta1.consultar_saldo()