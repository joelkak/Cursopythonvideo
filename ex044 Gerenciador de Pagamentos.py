print('{:=^40}'.format(' Lojas J(=´;´=)W '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
 [1] à vista dinheiro / cheque
 [2] à vista no cartão 
 [3] à 2x no cartão
 [4] à 3x ou mais  no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 /100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3 :
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} Sem JUROS '.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totalparc = int(input(' Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compŕas sera parcelada em {}x de R${:.2f} Com JUROS '.format(totalparc,parcela))
else:
    total = 0
    print('\033[0:43:41m OPÇÂO INVALIDA DE PAGAMENTO TENTE AS OPCOES DO MENU , TENTE NOVAMENTE \033[33m ')
print('Sua compra de R${:.2f} vai custa R${:.2f} no final '.format(preço , total))
