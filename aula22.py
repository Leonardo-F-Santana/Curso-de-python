# Operadores lógicos
# and - or - not
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for falso,
# a expressão inteira será avaliada naquele ValueErrorSão considerados False
# 0.0.0 '' FalseTambém existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E'or senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
