"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o numero que voce digitar: ')
try:
    print('str: ', numero_str)
    numero_float = float(numero_str) 
    print('float: ', numero_float)
    print(f'O dobro de {numero_str} é: {numero_float * 2}')
except:
    print('Isso não é um número')


