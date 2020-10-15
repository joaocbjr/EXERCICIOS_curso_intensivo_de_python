print('\n7.8 – Lanchonete:\n'
    ' Crie uma lista chamada sandwich_orders e a preencha com '
    'os nomes de vários sanduíches. Em seguida, crie uma lista '
    'vazia chamada finished_sandwiches. Percorra a lista de '
    'pedidos de sanduíches com um laço e mostre uma mensagem '
    'para cada pedido, por exemplo, Preparei  seu sanduíche de '
    'atum. À medida que cada sanduíche for preparado, transfira-o '
    'para a lista de sanduíches prontos. Depois que todos os '
    'sanduíches estiverem prontos, mostre uma mensagem que liste '
    'cada sanduíche preparado.\n')

sandwich_orders = ['dogão', 'bauru', 'vegetariano']
finished_sandwiches = []

while sandwich_orders:
    current_user = sandwich_orders.pop()
    print("Preparei seu sanduiche " + current_user.title()) 
    finished_sandwiches.append(current_user)

print("\nSanduiches preparados:") 
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
    sandwich_orders = []
    finished_sandwiches = []