peso = float(input('Qual é o seu peso ? (Kg) '))
altura = float(input('Qual é sua altura ? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está Abaixo do Peso Normal')
elif 18.5 <= imc < 25:
    print('Você está no Peso Normal')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você esta em Obesidade')
elif imc >= 40 :
    print("Obesidade Mórbida")
