#help interactive console for
    #ex:
help(print)
'''comando explicados atraves do help interative 

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
# escopo de variaveis
#exemplo
#escopo global e local,

def teste():
    x = 0
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#Programa Principal
'''n = 2
x = 0
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')'''

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('È par')
else:
    print('Não é par! È IMPAR!!')






