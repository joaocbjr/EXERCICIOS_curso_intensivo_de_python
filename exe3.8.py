print()
print('3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.\n• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.\n• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.\n• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.\n• Mostre que sua lista manteve sua ordem original exibindo-a.\n• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterara ordem da lista original.\n• Mostre que sua lista manteve sua ordem original exibindo-a novamente.\n• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.\n• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.\n• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.\n• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.')
print()

lugar = ['Florida', 'Dubai', 'Amsterdan', 'Portugal', 'Carira']

print(lugar, ' lista original')
print(sorted(lugar), ' lista com sorted')
print(lugar, ' lista sem sorted')

lugar.reverse()
print(lugar, ' lista com .reverse')
lugar.reverse()
print(lugar, ' lista com .reverse')
lugar.sort()
print(lugar, ' lista com .sort')
lugar.sort(reverse=True)
print(lugar, ' lista com .sort(reverse=True)')