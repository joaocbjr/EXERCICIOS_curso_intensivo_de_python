print()
print('4.11 – Minhas pizzas, suas pizzas:\n Comece com seu programa do Exercício 4.1(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte: \n• Adicione uma nova pizza à lista original.\n• Adicione uma pizza diferente à lista friend_pizzas.\n• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas  são:;  em  seguida,  utilize  um  laço for  para  exibir  a  primeira  lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.')
print()
pizzas = ['napolitano', '4 queijos', 'margerita']
friend_pizzas = pizzas[:]

pizzas.append('calabresa')
friend_pizzas.append('mussarela')
print('Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(pizza)
print()
print('As pizzas favoritas de meu amigo são:')
for pizza in friend_pizzas:
    print(pizza)
