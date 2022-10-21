cont = ('zero' , 'um', 'dois' , 'tres' , 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito',' dezenove', 'vinte')
while True:
    núm = int(input('Digite um número que esteja dentro de  0 a 20  '))
    if 0 <= núm <= 20:
        break
    print('Numero incorreto digite novamente', end='')
print('&*%' * 20)
print(f'Voce digitou o numero {cont[núm]} FIM DO PROGRAMA')
