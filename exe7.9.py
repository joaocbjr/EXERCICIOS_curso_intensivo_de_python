print('\n7.9 – Sem pastrami: \n'
    ' Usando a lista sandwich_orders do Exercício 7.8, '
    'garanta que o sanduíche de "pastrami" apareça na lista '
    'pelo menos três vezes. Acrescente um código próximo ao '
    'início de seu programa para exibir uma mensagem informando '
    'que a lanchonete está sem pastrami e, então, use um laço '
    'while para remover todas as ocorrências de "pastrami" '
    'e sandwich_orders. Garanta que nenhum sanduíche de '
    'pastrami acabe em finished_sandwiches.\n')

sandwich_orders = [
    'pastrami', 'dogão', 'pastrami', 'bauru', 
    'pastrami', 'vegetariano']
finished_sandwiches = []

while sandwich_orders:
    current_user = sandwich_orders.pop()
    print("Prepare o sanduiche " + current_user.title()) 
    finished_sandwiches.append(current_user)
print('\nDesculpe, estamos sem "pastami" no momento.')
print("\nSanduiches preparados:")

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

while 'pastami' in current_user:
    current_user.remove('pastami')
    print(current_user)
