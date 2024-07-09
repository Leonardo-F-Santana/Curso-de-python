# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
# L E O N A R D O
# -6-5-4-3-2-1

# nome = 'Leonardo'
# print('E' not in nome)

# nome = 'Leonardo'
# print('e' in nome)

# nome = 'Leonardo'
# print('Leo' not in nome)

# nome = 'Leonardo'
# print('Leo' in nome)

nome = input('Digite deu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')