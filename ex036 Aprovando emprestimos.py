casa = float(input('Valor da casa: R$ '))
salário = float(input('Salario do comprador: R$ '))
anos =  int(input('Quantos de financiamento ? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(' Para pagar uma casa de R$ {:.2f} em {}'.format(casa , anos), end=' ')
print(' a prestação sera de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
