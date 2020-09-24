print()
print(
    '5.5 – Cores de alienígenas #3:\n'
    'Escolha uma cor para um alienígena, como foi feito no '
    'Exercício 5.4, e escreva uma cadeia if-elif-else.\n'
    '• Se o alienígena for verde, mostre uma frase '
    'informando que o jogador acabou de ganhar cinco pontos.\n'
    '• Se o alienígena for amarelo, mostre uma frase '
    'informando que o jogador ganhou dez pontos.\n'
    '• Se o alienígena for vermelho, mostre uma frase '
    'informando que o jogador ganhou quinze pontos.\n'
    '• Escreva três versões desse programa, garantindo \n'
    'que cada mensagem seja exibida para a cor apropriada do alienígena.'
)
print()

alien_color = input(str('Entre Amarelo, verde ou vermelho. Escolha uma cor para o Alien: '))

if alien_color == 'verde':
    print('Você ganhou 05 pontos!')
elif alien_color == 'amarelo':
    print('Você ganhou 10 pontos!')
else:
    print('Você ganhou 15 pontos!')