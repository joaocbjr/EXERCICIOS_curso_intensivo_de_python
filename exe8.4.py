print('\n8.4 – Camisetas grandes:\n'
    ' Modifique a função make_shirt() de modo que as camisetas '
    'sejam grandes por default, com uma mensagem Eu amo Python. '
    'Crie uma camiseta grande e outra média com a mensagem '
    'default, e uma camiseta de qualquer tamanho com uma '
    'mensagem diferente.\n')

def make_shirt(frase, tamanho = 'G'):
    print('O tamanho da camiseta é ' + tamanho)
    print('Com a frase: ' + frase)

make_shirt(frase = 'Eu S2 Python\n')

def make_shirt(frase, tamanho = 'M'):
    print('O tamanho da camiseta é ' + tamanho)
    print('Com a frase: ' + frase)

make_shirt(frase = 'Eu S2 Python\n')

def make_shirt(frase = 'Efeito Pythonico', tamanho = 'P'):
    print('O tamanho da camiseta é ' + tamanho)
    print('Com a frase: ' + frase)

make_shirt()