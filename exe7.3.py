print('\n7.3 – Múltiplos de dez: \n'
    'Peça um número ao usuário e, em seguida, informe se o '
    'número é múltiplo de dez ou não.\n')

num = int(input('Digite um número: '))
if (num % 10 == 0):
    print('\nEste número é multiplo de 10\n')
else:
    print('\nEste número NÃO é multiplo de 10\n')