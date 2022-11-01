'''def lin():
    print('-' *30)

#Programa Principal
lin()
print('  CURSO EM VIDEO ')
lin()
print('  Aprenda Python  ')
lin()
print(' << J(=´;`=)E  >>')'''

'''def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)


#Programa Principal
titulo('  Curso em Video ')
titulo(' Aprenda Python  ')
titulo(' << J(=´;`=)E >>')'''

'''a = 4
b = 5
s = a + b
print(s)

a = 7
b = 8
s = a + b
print(s)

a = 1
b = 2
s = a + b
print(s)'''

'''def soma(a, b):
    print(f' A = {a} e B = {b}' )
    s = a + b
    print(f'A soma de A + B = {s}')


#Programa Principal
soma(b=4, a=5)
soma(7, 8)
soma(1, 2)'''

'''def contador(* núm):
    #for valor in núm:
        #print(f'{valor}' , end=' ')
        tam = len(núm)
        print(f'Recebi os valores {núm} e são ao todo {tam} números')
    #'print('FIM')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)


