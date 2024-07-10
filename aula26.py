"""
Formatação básica de strings
s - sting
d - int
f - float
.<número de digitos>f
x ou X - hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:1^10}')
print(f'{1000.45375226:,.2f}')
print(f'O hexadecimal de 1500 é: {1500:X}')
print(f'{variavel!a}')
