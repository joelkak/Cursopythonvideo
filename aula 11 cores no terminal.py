print('\033[7;33;44m Olá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32;45m{}\033[m e \033[31;47m{}\033[m !!!'.format(a , b))

nome = 'Joel Silverio'
print(' Olá ! Muito prazer em te conhecer, {}{}{}!!! '.format('\033[7;35;40m' , nome, '\033[m'))
cores  = {'limpa':'\033[m' ,
          'azul' : '\033[34m',
          'amarelo': '\033[33m' ,
          'pretoebranco':'\033[7;30m'}
print('Olá muito prazer em te conhecer , {}{}{}!!'.format(cores['pretoebranco'], nome , cores['limpa'] ))
