nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
média = (nota1 + nota2 ) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f} '.format(nota1 , nota2 , média))
if 7 > média >= 5:
    print('O aluno estsa em RECUPERAÇÂO.')
elif média < 5:
    print('O aluno esta REPROVADO.')
else:# elif media >= 7: tambem funga
    print('O aluno esta APROVADO')

