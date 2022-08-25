velocidade =  float(input('Qual é a velocidade do carro ? ')) # esquema baixo chamdo de condição simples
if velocidade > 80:
    print('Multado! Você excedu o limite de velocidade permitido que é de 80km/h')
    multa = (velocidade- 80) * 7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia ! Dirija com segurança')
