print()
print(
    '5.4 – Cores de alienígenas #2:\n'
    'Escolha uma cor para um alienígena, como foi feito no '
    'Exercício 5.3, e escreva uma cadeia if-else.\n'
    '• Se a cor do alienígena for verde, mostre uma frase '
    'informando que o jogador acabou de ganhar cinco pontos '
    'por atingir o alienígena.\n'
    '• Se a cor do alienígena não for verde, mostre uma frase '
    'informando que o jogador acabou de ganhar dez pontos.\n'
    '• Escreva uma versão desse programa que execute o bloco '
    'if e outro que execute o bloco else.'
)
print()

alien_color = input('Escolha uma cor para o Alien: Amarelo, verde ou vermelho', alien_color))

if alien_color == 'verde':
    print('Você ganhou 05 pontos!')
else:
    print('Você ganhou 10 pontos!')