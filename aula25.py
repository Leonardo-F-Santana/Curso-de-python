"""
Interpolação básica de strings
s - string 
d e i - int
f - float
x e X - hexadecimal (0123456789ABCDEF)
"""
nome = 'Leonardo'
preco = 5500.86123
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))