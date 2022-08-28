frase = str(input('Digite uma frase:  ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso= junto [::-1] #forma simples do codigo macete do fatiamento ...

'''for letra in range(len(junto) -1 , -1 , -1):
    inverso += junto[letra]''' # sendo esta a forma feita com o laço for ...mas compĺexa.

print('O inverso de {} é {} '.format(junto , inverso))
if inverso == junto:
    print('Temos um Palindromo! ')
else:
    print('A frase digitada não é um palindromo! ')




print(' Voce digitou a frase {}'.format(frase))


