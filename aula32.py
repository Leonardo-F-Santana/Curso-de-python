'''
Faça um programa que peça ao usuario um numro inteiro,
informe se este número é par ou ímpar. Caso o usuario não digite um número
inteiro, informe que não é um número inteiro.
'''
# numero = input('Digite um número: ')

# try:
#     numero = int(numero)
#     if numero % 2 == 0:
#         print(f'O número {numero} é par!')
#     else:
#         print(f'O número {numero} é ímpar!')
# except:
#     print('Você não digitou um número inteiro!')



'''
Faça um programa que pergunte a hora ao usuário e,
baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, boa tarde 12-17, boa noite 18-23
'''
nome = input('Digite seu nome: ')
hora = int(input('Digite a hora: '))
if 0<= hora <=11:
    print(f'Bom dia {nome}!')
elif 12<= hora <= 18:
    print(f'Boa tarde {nome}!')
else:
    print(f'Boa noite{nome}!')   
# hora = input('Digite a hora')
# try:
#     hora = int(hora)
#     if hora == 0 :
#         print('Bom dia!')




'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menosm escreva "Seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; naior que 6m escreva "Seu nome é muito grande"
'''