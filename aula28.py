"""
Exercício:
Peça o usuario para digitar seu nome
Peça o usuario para digitar sua idade
Se o nome e idade forem digitados:
        Exiba:
            Seu nome é:
            Seu nome invertido é:
            Seu nome contém (ou não) espaços
            Seu nome tem N letras
            A primeira letra do seu nome é:
            A ultima letra do seu nome é:
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios!"
"""
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'Seu nome é: {nome}')
print(f'A idade do {nome} é: {idade}')
print(f'seu nome invertido é: {nome[::-1]}')
print(f'{nome} contem {len(nome)} caracteres')
print(f'A primeira letra de {nome} é: {nome[0]}')
print(f'A ultima letra de {nome} é : {nome[-1]}')
if ' ' in nome:
    print(f'{nome} contém {len(' ')} espaços!')
else:
    print(f'Não contem espaços!')