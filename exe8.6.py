print('\n8.6 – Nomes de cidade:\n'
    ' Escreva uma função chamada city_country() que aceite o '
    'nome de uma cidade e seu país. A função deve devolver uma '
    'string formatada assim: "Santiago, Chile".\n'
    'Chame sua função com pelo menos três pares cidade-país '
    'e apresente o valor devolvido.\n')

def city_country():
    #Devolve cidade, país.
    while True:
        if city == s:
            city = str(input('Deseja inserir mais cidades [s/n]:'))
            dado = str(input('Digite uma cidade: ', 'e o país: '))
        else:
            print(dado)
        
city_country()