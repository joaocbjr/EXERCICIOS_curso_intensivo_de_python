print('\n8.7 – Álbum:\n'
    ' Escreva uma função chamada make_album() que construa um '
    'dicionário descrevendo um álbum musical. A função deve '
    'aceitar o nome de um artista e o título de um álbum e '
    'deve devolver um dicionário contendo essas duas informações. \n'
    'Use a função para criar três dicionários que representem '
    'álbuns  diferentes. Apresente cada valor devolvido para '
    'mostrar que os dicionários estão armazenando as informações '
    'do álbum corretamente.\n Acrescente um parâmetro opcional '
    'em make_album() que permita armazenaro número de faixas em '
    'um álbum. Se a linha que fizer a chamada incluir um valor '
    'para o número de faixas, acrescente esse valor ao dicionário '
    'do álbum. Faça pelo menos uma nova chamada da função incluindo '
    'o número de faixa sem um álbum.\n')

def make_album():
    '''Descreve um album musical'''
    album = {'artista': nome_artista, 'album': titulo_album}
    return album




