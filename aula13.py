# nome ='Leonardo'
# altura = 1.80
# peso = 95
# imc = peso / (altura * altura)

# "f-strings"
# linha_1 = f'{nome} tem {altura:.2f} de altura'
# linha_2 = f'pesa {peso} quilos e seu imc é'
# linha_3 = f'{imc:.2f}'

# print(linha_1)
# print(linha_2)
# print(linha_3)
nome = input("Digite seu nome: ") 
sobrenome = input("Digite seu sobrenome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso:"))
imc= peso / (altura * altura)

print(f'O {nome} {sobrenome}, possui altura {altura:.2f}m, peso {peso}Kg e seu IMC é de: {imc:.2f}')

if imc <=18.5:
    print(nome + sobrenome, "Está abaixo do peso!")
elif imc <=24.9:
    print(nome + sobrenome, "Está em seu peso ideal!")
elif imc <=29.9:
    print(nome + sobrenome, "Está acima do peso!")
elif imc <=34.9:
    print(nome + sobrenome, "Obesidade Grau I")
elif imc <=39.9:
    print(nome + sobrenome, "Obersidade Grau II")
else:
    print(nome + sobrenome, "Obesidade Grau III")