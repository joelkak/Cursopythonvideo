def fatorial(n , show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O numeor a ser calculado.
    :param show: (opicional) mostras ou não a conta.
    :return: O valor fatorial de um numeor n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c >1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
help(fatorial)
