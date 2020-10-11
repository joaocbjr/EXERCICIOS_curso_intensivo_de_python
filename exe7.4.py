print('\n7.4 – Ingredientes para uma pizza:\n'
' Escreva um laço que peça ao usuário para fornecer uma série '
'de ingredientes para uma pizza até que o valor "quit" seja '
'fornecido. À medida que cada ingrediente é especificado, '
'apresente uma mensagem informando que você acrescentará esse '
'ingrediente à pizza.\n')

prompt = 'Adicione ingredientes à pizza ou digite "quit" para encerrar o programa. '
mensagem = ''
while mensagem != 'quit':
    mensagem = input(prompt)
    print(mensagem)