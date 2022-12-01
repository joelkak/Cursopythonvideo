from ex108 import moeda

p = float(input('digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.moeda(moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.moeda(moeda.dobro(p)}')
print(f'Aumentando 10% temos R${moeda.moeda(moeda.aumentar(p, 10)}')
