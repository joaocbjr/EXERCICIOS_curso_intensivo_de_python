print('\n6.8 – Animais de estimação:\n'
    ' Crie vários dicionários, em que o nome de cada dicionário '
    'seja o nome de um animal de estimação. Em cada dicionário, '
    'inclua o tipo do animal e o nome do dono. Armazene esses '
    'dicionários em uma lista chamada pets. Em seguida, percorra '
    'sua lista com um laço e, à medida que fizer isso, apresente '
    'tudo que você sabe sobre cada animal de estimação.\n')
pets = {
    'preta' : {'tipo': 'galinha', 'dono': 'João'}
    'lilica' : {'tipo': 'cachorro', 'dono': 'Celso'}
    'vovó' : {'tipo': 'gato', 'dono': 'Driele'}
    'elves' : {'tipo': 'porco', 'dono': 'Adenilton'}
}

for name, tipo, dono  in pets.items():
    print()
