pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Joel'
#'''print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.items())
#print(pessoas.keys())
#print(pessoas.values())
for k , v in pessoas.items():
    print(f'{k} = {v}')


