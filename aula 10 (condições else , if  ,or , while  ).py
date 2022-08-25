'''nome = str(input(' Qual seu nome ? '))
if nome == 'Joel':
    print('Que nome lindo você tem !')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}! '.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABENS' if m >= 6 else 'ESTUDE MAIS!') # forma mais resumida do codigo condição simplificada
#forma mais simples do codigo e composta

"""if m >= 6.0:
    print('Sua média foi boa! Parabens Cabeça de Bagre! ')
else:
    print('Sua média foi ruim! Va estudar mais zazazento')"""




