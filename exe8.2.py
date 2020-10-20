print('\n8.2 – Livro favorito:\n'
    ' Escreva uma função chamada favorite_book() que aceite um '
    'parâmetro title. A função deve exibir uma mensagem como '
    'Um dos meus livros favoritos é Alice no país das maravilhas. '
    'Chame a função e não se esqueça de incluir o título do '
    'livro como argumento na chamada da função.\n')



def favorite_book():   #Exibe o livro favorito
    livro = str(input('Digite o nome do livro que gosta: '))
    print('Um dos meus livros favoritos é ' + livro.title())

favorite_book()