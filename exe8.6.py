print('\n8.6 – Nomes de cidade:\n'
    ' Escreva uma função chamada city_country() que aceite o '
    'nome de uma cidade e seu país. A função deve devolver uma '
    'string formatada assim: "Santiago, Chile".\n'
    'Chame sua função com pelo menos três pares cidade-país '
    'e apresente o valor devolvido.\n')

def city_country():
# Devolve cidade, país.
    lugar = {}
# Define uma flag para indicar que inserção de dados está ativa
    incluir = True
    while incluir:
# Pede para incluir nome da cidade e do país
        cidade = input('\nDigite uma cidade: ')
        país = input('Digite seu respectivo país: ')
# Armazena as respostas no dicionário
        lugar[cidade] = país
# pergunta se vai inserir mais lugares
        repeat = input('Deseja inserir mais cidades? [s|n] ')
        if repeat == 'n':
            incluir = False
# A lista de lugares foi concluída.
# Mostra os resultados
    print('\n -=-=-=- City_Country -=-=-=-')
    for cidade, país in lugar.items():
        print(cidade.title() + ', ' + país.title())

city_country()