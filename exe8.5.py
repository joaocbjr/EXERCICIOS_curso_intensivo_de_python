print('\n8.5 – Cidades:\n'
    ' Escreva uma função chamada describe_city() que aceite o '
    'nome de uma cidade e seu país. A função deve exibir uma '
    'frase simples, como Reykjavik está localizada na Islândia. '
    'Forneça um valor default ao parâmetro que representa o país. '
    'Chame sua função para três cidades diferentes em que pelo '
    'menos uma delas não esteja no país default.\n')

def describe_city(cidade = 'Bueno Aires', país = 'Argentina'):
    print(cidade + ' está localizado na ' + país)

describe_city()

def describe_city(cidade, país = 'Brasil'):
    print(cidade + ' está localizado no ' + país)

describe_city(cidade = 'Alagoas')
describe_city(cidade = 'Sergipe')


