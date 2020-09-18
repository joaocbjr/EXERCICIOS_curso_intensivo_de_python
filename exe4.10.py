print()
print('4.10  –  Fatias:\n Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:\n• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.\n• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.\n• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.')
print()

convidado = ['Vovó', 'Mãe', 'Pai', 'Bernardo']

convidado.insert(1, 'Ester')
convidado.insert(4, 'Dona Chica')
convidado.append('Roberto')

print('Exercício 3.6 temos a seguinte lista: \n',convidado)
print()
print('Os três primeiros itens da lista são:', convidado[:3])
print()
print('Os três itens do meio da lista são:', convidado[3:6])
print()
print('Os três últimos itens da lista são:', convidado[4:])