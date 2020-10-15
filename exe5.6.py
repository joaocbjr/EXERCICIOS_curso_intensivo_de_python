print('\n5.6 – Estágios da vida:\n'
    ' Escreva uma cadeia if-elif-else que determine estágio '
    'da vida de uma pessoa. Defina um valor para a variável '
    'age e então: \n'
    '• Se a pessoa tiver menos de 2 anos de idade, '
    'mostre uma mensagem dizendo que ela é um bebê.\n'
    '• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, '
    'mostre uma mensagem dizendo que ela é uma criança.\n'
    '• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, '
    'mostre uma mensagem dizendo que ela é um(a) garoto(a).\n'
    '• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, '
    'mostre uma mensagem dizendo que ela é um(a) adolescente.\n'
    '• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, '
    'mostre uma mensagem dizendo que ela é adulto.\n'
    '• Se a pessoa tiver 65 anos ou mais, '
    'mostre uma mensagem dizendo que essa pessoa é idoso.\n'
)

age = input(int('Qual é a sua idade: '))

if age < 2:
    print('Você é um bebê.')
elif age < 4:
    print('Você é uma criança.')
elif age < 13:
    print('Você é um(a) garoto(a).')
elif age < 20:
    print('Você é um(a) adolecente.')
elif age < 65:
    print('Você é adulto(a).')
else age > 64:
    print('Você é idoso.')

