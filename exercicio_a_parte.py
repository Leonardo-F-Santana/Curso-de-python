# Imprimir o maior numero

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo numero: '))

if numero_1 > numero_2:
    print(f'{numero_1} é maior que o {numero_2}')

else:
    print(f'{numero_2} é maior que {numero_1}')




# Verificação de positivo ou negativo

numero = int(input('Digite um número: '))

if numero < 0:
    print('Este número é negativo!')

elif numero >0:
    print('Este é um número positivo!')

else:
    print('Este número é nulo!')




# Tomada de decisão simple:


parentesco = input('Digite o grau de parentesco: ')

if parentesco == "Pai" or 'Mãe':
    print('Você pode sentar na mesa azul!')

else:
    print('Você tem que procurar outra mesa pra sentar!')