inventario = {
'itens': {'hp_potion': {5}, 'flechas': {21}, 'tomo_feitico-fireball': {1}},
'armas': {'principal': {'Espada de Aço Forjado (Ótimo)'}, 'secundaria': {'Adaga de Aço Polido'}, 'ranged': {'Arco de Caça Reforçado'}},
'armadura': {'cabeca': {'Elmo de Aço (Ótimo)'}, 'peitoral': {'Peitoral de Ferro'}, 'calca': {'Calças de Lã'}, 'botas': {'Chinelo de Dedo'}},
'mochila': {'Lanterna (Bem desgastada)': {67}}
}

dicionario_teste = {'nome':'Erick','idade':'18','sexo':'M','gosta_de':'Computadores, Aviões'}

for k, v in dicionario_teste.items():
    print(k, v)

for keys, values in inventario.items():
    print(f'\n{keys}:{values}')

def celsius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return print(f'O valor de {fahrenheit}ºF em ºC é: {c:.2f}')

celsius(77)
