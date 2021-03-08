print('\n8.7 – Álbum:\n'
    ' Escreva uma função chamada make_album() que construa um '
    'dicionário descrevendo um álbum musical. A função deve '
    'aceitar o nome de um artista e o título de um álbum e '
    'deve devolver um dicionário contendo essas duas informações. \n'
    'Use a função para criar três dicionários que representem '
    'álbuns  diferentes. Apresente cada valor devolvido para '
    'mostrar que os dicionários estão armazenando as informações '
    'do álbum corretamente.\n Acrescente um parâmetro opcional '
    'em make_album() que permita armazenar o número de faixas em '
    'um álbum. Se a linha que fizer a chamada incluir um valor '
    'para o número de faixas, acrescente esse valor ao dicionário '
    'do álbum. Faça pelo menos uma nova chamada da função incluindo '
    'o número de faixa sem um álbum.\n')

def make_album():
# Devolve artista, album.
    nome = {}          
# Define uma flag para indicar que inserção de dados está ativa
    incluir = True
    while incluir:
# Pede para incluir nome do artista e do album
        artista = input('\nDigite o nome do artista: ') 
        album = input('Digite seu album: ')
# Armazena as respostas no dicionário
        nome[artista] = album
# pergunta se vai inserir mais albuns
        repeat = input('Deseja inserir mais algum album? [s|n] ')
        if repeat == 'n':
            incluir = False
# A lista de albuns foi concluída.
# Mostra os resultados
    print('\n -=-=-=- Dicionário de Album musical -=-=-=-')
    for artista, album in nome.items():
        print(artista.title() + ', ' + album.title())

make_album()