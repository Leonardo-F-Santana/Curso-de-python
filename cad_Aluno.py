aluno = input('Digite o nome do aluno: ')

nota1 = float(input(f'Digite a primeira nota do {aluno} '))
nota2 = float(input(f'Digite a segunda nota do {aluno} '))
nota3 = float(input(f'Digite a terceira nota do {aluno} '))
nota4 = float(input(f'Digite a quarta nota do {aluno} '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media <6:
    print(f'O aluno {aluno} ficou com média {media}, com isso está REPROVADO!')
elif 6<= media <7:
    print(f'O aluno {aluno} ficou com média {media}, com isso está de RECUPERAÇÃO!')
else:
    print(f'O aluno {aluno} ficou com média {media}, com isso está APROVADO!')