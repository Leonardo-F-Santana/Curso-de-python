x=int(imput("Quantos elementos tem os vetores? "))
vet1=[ ]*x
vet2=[ ]*x
vet3=[ ]*x
for i in range(x+1):
vet1[i]=int(input(f"Digite o valor do {i+1}º elemento"))
for i in range(x):
vet2[i]=int(input(f"Digite o valor do {i+1}º elemento"))
for i in range(x):
vet3=vet1[i]+vet2[i]
print(f"(vet3)")