print('\n7.5 – Ingressos para o cinema: \n'
    ' Um cinema cobra preços diferentes para os ingressos de '
    'acordo com a idade de uma pessoa. Se uma pessoa tiver '
    'menos de 3 anos de idade, o ingresso será gratuito; se '
    'tiver entre 3 e 12 anos, o ingresso custará 10 dólares; '
    'se tiver mais de 12 anos, o ingresso custará 15 dólares. '
    'Escreva um laço em que você pergunte a idade aos usuários '
    'e, então,informe-lhes o preço do ingresso do cinema.\n')

while True:
    ingre = int(input('Quer comprar ingreço? [1 = Sim | 0 = Não]: '))
    if ingre == 1:
        idade = int(input('Informe a sua idade: '))
        if idade < 3:
            print('Ingresso gratuito\n')
        elif idade < 12:
            print('Ingresso custa US$ 10,00\n')
        elif idade > 11:
            print('Ingresso custa US$ 15,00\n') 
        else:
            print('Informe uma idade válida')
    else:
        break
print('Obrigado, volte sempre!')