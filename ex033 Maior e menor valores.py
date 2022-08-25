a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando o menor
if a <b and a < c:
    menor = a
if b <c and b < a :
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
if a > b and a > c:
    maior = a
if b > c and b > a :
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))