print("**********************")
print("IRRF - 2024")
print("**********************")

nome = input("Digite o nome: ")
renda = float(input("Digite a renda: "))
aliquota = renda
if (aliquota<1903.00):
   classificacao = "insento"
elif(aliquota<2826.65):
    classificacao = "7.5%"
elif(aliquota<3751.05):
    classificacao = "15%"
elif(aliquota<4664.68):
    classificacao = "22.5%"
else:
    classificacao = "27.5%"

print(f"O(a) {nome} tem um percentual de aliquota no valor de: {classificacao}")