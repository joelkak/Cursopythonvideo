def notas(*n, sit=False):
    """
    -> Função para analisar notas e situaçoes de varios alunos.
    :param n: uma ou mais nots dos alunos (aceita várias)
    :param sit: Valor opcional , indicando se deve ou não adcionar a situação
    :return: dicionario com varias informaçoes sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
