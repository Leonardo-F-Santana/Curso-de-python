# valor=float(input("Digite o valor da casa:"))
# salario=float(input("Digite o salário:"))
# anos=int(input("Quantos anos para pagar:"))
# meses = anos * 12
# prestacao = valor / meses
# if prestacao > salario * 0.3:
#     print("Infelizmente você não pode obter o empréstimo")
# else:
#     print(f"fValor da prestação: R$ {prestacao:.2f} Empréstimo OK" )


# Fazer um programa que leia duas notas de alunos, calcular a média desses alunos e imprimir quantos são aprovados (média maior ou igual a 7,0),
# quantos estão em exame final (média entre 4,0 e 7,0) ou quantos estão reprovados (média menor que 4,0). O programa deve solicitar quantos alunos possui a turma
# e imprimir um quantitativo em cada um dos três casos. EXIBIR O CÓDIGO COM O PRINT RODANDO

aluno = input('Digite o nome do aluno: ')
nt1 = float(input("Digite a primeira nota do aluno: "))
nt2 = float(input("Digite a segunda nota do aluno: "))
media = (nt1 + nt2) / 2
if media > 7.0:
    print(f'O aluno {aluno}, ficou com média {media} e foi aprovado!')
elif media >5:
    print(f'O aluno {aluno}, ficou com média {media} e ficou de recuperação!')
else:
    print(f'O aluno {aluno}, ficou com média {media} e foi reprovado!')