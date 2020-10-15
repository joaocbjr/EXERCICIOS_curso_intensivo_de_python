print('\nPodemos pedir a quantidade de entrada que for necessária a cada passagem por um laço while. Vamos criar um programa de enquete em que cada passagem pelo laço solicita o nome do participante e uma resposta. Armazenaremos os dados coletados em um dicionário, pois queremos associar cada resposta a um usuário em particular:\n')

responses = {}
# Define uma flag para indicar que a enquete está ativa 
polling_active = True
while polling_active:
# Pede o nome da pessoa e a resposta 
    name = input("\nWhat is your name? ")
    response = input("Which mountain would youlike to climb someday? ")
# Armazena a resposta no dicionário
    responses[name] = response
# Descobre se outra pessoa vai responder à enquete
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# A enquete foi concluída. Mostra os resultados
print("\n--- Poll Results---")
for name, response in responses.items():
    print(name + " wouldlike to climb " + response + ".")
