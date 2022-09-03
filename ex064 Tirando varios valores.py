núm = cont = soma = 0
núm = int(input('Digite um numero [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont , soma))

