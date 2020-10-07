print('\n7.2 – Lugares em um restaurante: \n'
    'Escreva um programa que pergunte ao usuário quantas '
    'pessoas estão em seu grupo para jantar. Se a resposta '
    'for maior que oito, exiba uma mensagem dizendo que eles '
    'deverão esperar uma mesa. Caso contrário, informe que '
    'sua mesa está pronta.\n')

pessoas = int(input('Quantas pessoas estão em seu grupo para jantar: '))
if pessoas < 8:
    print('\nSua mesa esta pronta.\n')
else:
    print('\nDesculpe. Deverão esperar uma mesa.\n')
