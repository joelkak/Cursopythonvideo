soma = 0 # Acumulaador soma numeros
cont = 0 # coonta os numeros
for c in range(1 , 501,  2 ):
    if c % 3 == 0:
        cont = cont + 1 # pode ser usado += aqui tambem (soma += c) codigo enxuto
        soma = soma + c # aqui tambem pode ser usado += (cont += 1) codigo enxuto
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
