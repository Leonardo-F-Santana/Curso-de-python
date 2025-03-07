# contador = 0

# while contador <=100:
#     contador +=1

#     if contador == 5:
#         print('Vou pular o 5!')
#         continue

#     print(contador)

#     if contador == 99:
#         break



qtd_linhas = 5
qtd_colunas = 5

linhas = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna +=1
    linha +=1

print('Acabou')