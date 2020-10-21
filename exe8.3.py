print('\n8.3 – Camiseta:\n'
    'Escreva uma função chamada make_shirt() que aceite um '
    'tamanho e o texto de uma mensagem que deverá ser estampada '
    'na camiseta. A função deve exibir uma frase que mostre '
    'o tamanho da camiseta e a mensagem estampada.\n\tChame a '
    'função uma vez usando argumentos posicionais para criar '
    'uma camiseta. Chame a função uma segunda vez usando argumentos '
    'nomeados.\n')

def make_shirt(tamanho, frase):
    print('O tamanho da camiseta é ' + tamanho)
    print('Com a frase: ' + frase)

make_shirt('M', 'Jesus salva.\n')

def make_shirt(tamanho = 'G', frase = 'O cordeiro venceu.'):
    print('O tamanho da camiseta é ' + tamanho)
    print('Com a frase: ' + frase)

make_shirt()