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

# resultado = int((x + int(y)) / z + lst[1] * len(y)) + 10.0 

# print(resultado) 

class Animal: 

    def __init__(self, nome): 

        self.nome = nome 

    def emitir_som(self): 

        print("Som genérico") 

class Cachorro(Animal): 

    def emitir_som(self): 

        print("Au au") 

class Gato(Animal): 

    def emitir_som(self): 

        print("Miau") 

animal1 = Animal("Rex") 

animal2 = Cachorro("Totó") 

animal3 = Gato("Minhoca") 

 

animal1.emitir_som() 

animal2.emitir_som() 

animal3.emitir_som() 