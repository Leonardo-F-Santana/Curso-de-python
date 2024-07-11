"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[0:5]) # Começa do indice 0 ou
 # Começa do indice 0 ou
# a primeira letra do "Olá mundo" até a 5ª letra

variavel = 'Olá mundo'
print(len(variavel[2:8])) # A função len faz a checagem da quantidade

variavel = 'Olá mundo'
print(variavel[0:8:2]) # A função com 2 :, faz a "pulagem" de caractere
 # A função com 2 :, faz a "pulagem" de caractere

# [0:8:2] 0 = começo do indice; 8 = final do indice; 2 = de quantas em quantas casas ele vai pular

variavel = 'Olá mundo'
print(variavel[::-1]) # quando coloca numero negativo na "pulagem" ele inverte a contagem