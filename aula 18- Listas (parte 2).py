#galera = [['Joao', 19], ['Ana',33 ],['Joaquim', 13],['Maria', 45], ['Joe', 44]]

#print(galera[2][1])
#for p in galera:
#print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

print(galera)
