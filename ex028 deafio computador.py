from random import randint
from time import sleep

computador = randint(0 , 5) # faz o computador "Pensar " (sortear)"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5 . Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numeor eu pensei?'))# jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer ! ')
else:
    print('Ganhei! Eu pensei no numero {} e não no {} !'.format(computador , jogador))



