print()
print('3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.\n• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha quemostre  uma  mensagem  informando  que  você  pode  convidar  apenas  duas pessoas para o jantar.\n• Utilize pop() para remover os convidados de sua lista, um de cada vez, atéque apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.\n• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.\n• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa:')
print()

convidado = ['Vovó', 'Mãe', 'Pai', 'Bernardo']
mensagem = "Ti convido pra jantar "

print(mensagem + convidado[0])
print(mensagem + convidado[1])
print(mensagem + convidado[2])
print()
print('O convidado(a) ' + convidado[0] + ' não poderá comparecer')
print()
print(mensagem + convidado[1])
print(mensagem + convidado[2])
print(mensagem + convidado[3])
print()
print('Queridos convidados, foi encontrado uma mesa maior e vamos aumentar o número de convidados')
print()

convidado.insert(1, 'Ester')
convidado.insert(4, 'Chica')
convidado.append('Roberto')

print(mensagem + convidado[1])
print(mensagem + convidado[2])
print(mensagem + convidado[3])
print(mensagem + convidado[4])
print(mensagem + convidado[5])
print(mensagem + convidado[6])
print()
print('Queridos peço desculpas, tivemos problema e só posso convidar duas pessoas')

desconvide = 'Peço desculpas mas terei que ti desconvidar '
print(convidado)

print(desconvide + convidado[1])
convidado.pop(1)
print(desconvide + convidado[2])
convidado.pop(2)
print(desconvide + convidado[3])
convidado.pop(3)
print(desconvide + convidado[4])
convidado.pop(4)
print()
print('O convite está de pé ' + convidado[1])
print('O convite está de pé ' + convidado[2])
del convidado[1]
del convidado[2]
print(convidado)