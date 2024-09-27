n=int(input("Qual a quantidade de números a serem digitados?\n"))
soma = 0
for i in range(1, n+1):
   num = int(input(f"Digite o valor do {i}º número: \n"))
   soma+=num
print(f"A soma dos {n} números digitados é: {soma}")
#fim


n=int(input("Qual a quantidade de números a serem digitados?\n"))
produto = 1
for i in range(1, n+1):
   num = int(input(f"Digite o valor do {i}º número: \n"))
   produto *= num
print(f"O produto dos {n} números digitados é: {produto}")

#fim


n=int(input("Quantos alunos tem matriculados na turma?\n"))
soma=0
for i in range(1, n+1):
   nome=input(f"Digite o nome do {i}º aluno\n")
   idade=int(input(f"Digite a idade do {i}º aluno\n"))
   soma+=idade
media=soma/n
print(f"A media das idades dos {n} alunos é {media:.2f}")
#fim


valor=int(input("Entre com o numero para saber a tabuada:"))
print("*" * 18)
print(f"Tabuada de {valor}")
print("*"*18)
for i in range(11):
   print(f"{valor} x {i}={i*valor}")

#fim

continua = "s"
somaidade = 0
n=0
while (continua == "s" or continua =="S"):
    nome = input(f"Digite o nome do {n+1}º aluno")
    idade=int(input(f"Digite a idade do {n+1}º aluno:"))
    somaidade=somaidade +idade
    continua = input("Deseja continuar cadastrasndo? Digite (s) para sim e (n) para não")
    n=n+1
    print(f"Foram cadastrado {n} alunos")
    mediaidade=somaidade/n
    print(f"A média de idade da turma é {mediaidade:.2f}")

#fim


nome = 'leo'
print(nome.capitalize())