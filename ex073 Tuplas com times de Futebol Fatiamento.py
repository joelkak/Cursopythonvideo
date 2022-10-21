Times = ('PALMEIRAS' ,'INTERNACIONAL' ,'FLAMENGO','FLUMINENSE','CORINTHIANS','ATHLETICO-PR',
         'ATLÉTICO-MG','AMÉRICA-MG','GOIÁS','SANTOS','RED BULL BRAGANTINO','BOTAFOGO','SÃO PAULO',
         'CEARÁ','FORTALEZA','CORITIBA','CUIABÁ','AVAÍ,ATLÉTICO-GO','JUVENTUDE')
print('=-*' * 20)
print(f'lista de times do Brasileirão: {Times}')
print('-*' * 20)
print(f'Os 5 primeiros são {Times[0:5]}')
print('=-*' * 20)
print(f'Os Ultmos 4 são {Times[-4:]} ')
print('=-*' * 20)
print(f'Times em ordem alfabetica: {sorted(Times)}')
print('=-*' * 20)
print(f'O SANTOS está na {Times.index("SANTOS")+1}ª posição')

