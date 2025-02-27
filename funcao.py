def situacao_aluno(media):
    if media <6:
        situacao = 'Reprovado'
    else:
        situacao = 'Aprovado'
    return situacao

for i in range(3):
    nome = input(f'Digite o nome do aluno(a): ')
    nota1 = float(input(f'Digite a nota do 1º bimestre do(a) {nome}: '))
    nota2 = float(input(f'Digite a nota do 2º bimestre do(a) {nome}: '))
    nota3 = float(input(f'Digite a nota do 3º bimestre do(a) {nome}: '))
    nota4 = float(input(f'Digite a nota do 4º bimestre do(a) {nome}: '))
    media = (nota1 + nota2 + nota3 + nota4)/4

    print(f'{nome} ficou com media {media:.2f}')
    situacao = situacao_aluno(media)
    print(f'Com essa media, {nome} ficou {situacao}')