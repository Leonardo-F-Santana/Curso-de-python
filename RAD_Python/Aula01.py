def exemplo01():
    arquivo = open('texto.txt', 'w')
    arquivo.writelines(['Leo', '\nSavana', '\nKaio', '\nSandy', '\nRycardo'])
    arquivo.close()

def exemplo02():
    arquivo = open('texto.txt', 'w')
    print('texto.txt')
    arquivo.close()

def exemplo03():
    caminho_arquivo = 'texto.txt'

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('Essa é a primeira linha.\n')
        arquivo.write('Essa é a segunda linha.\n')

        linhas = ['Essa é a primeira linha em uma lista.\n', 'Essa é a primeira linha em uma lista.\n' ]

    

    exemplo01()
    exemplo02()
    exemplo03()

    caminho_arquivo = 'texto.txt'
    arquivo = open(caminho_arquivo, 'r')

    linha1 = arquivo.readline()
    print(f'Linha 1: {linha1}')
    linha2 = arquivo.readline()
    print(f'Linha 2: {linha2}')

    arquivo.close()

    arquivo = open(caminho_arquivo, 'r')

    linha = arquivo.readlines()
    for i, linha in enumerate(linha, start =1):
        print(f'Linha {i}: {linha}')