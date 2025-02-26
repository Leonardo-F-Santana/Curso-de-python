# class Computador():
#     def __init__(self, marca, memoria_Ram, Placa_de_Video, valor):
#         self.marca = marca
#         self.memoria_Ram = memoria_Ram
#         self.Placa_de_Video = Placa_de_Video
#         self.valor = valor
#         pass

# computador1 = Computador('Asus', '16Gb', 'Nvidia', 'R$1800.00')
# computador2 = Computador('Dell', '32Gb', 'Gforce', 'R$3500.00')

# print(computador1.marca,computador1.memoria_Ram,computador1.Placa_de_Video,computador1.valor)
# print(computador2.marca,computador2.memoria_Ram,computador2.Placa_de_Video,computador2.valor)


class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
    def vendeu (self, vendas):
        self.vendas = vendas
    def bateu_meta (self, meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu a meta de vendas!')
        else:
            print(self.nome, 'Não bateu a meta de vendas!')

vendedor1 = Vendedor('Leonardo')
vendedor1.vendeu(12000)
vendedor1.bateu_meta(600)

print(vendedor1.vendas)