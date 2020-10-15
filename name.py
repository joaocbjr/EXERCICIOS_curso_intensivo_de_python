'''print()
name = 'joão correia bezerra junior'
print(name.title()) #retorna a primeira letra maiuscula
print(name.upper()) #retorna todas as letras MAIUSCULAS
print(name.lower()) #retorna todas as letras minusculas
lista.append('novo item') #APPEND inclui um novo item a lista
robi = 'programador'

futuro = name + " " + robi
print(futuro)
print('Olá, ' + futuro.title() + '!')

print()'''

# calculo de média
'''
total = 0
conta = 0
while (True):
    inp = input("Digite o número: ")
    if inp == 'n': break
    valor = float(inp)
    total = total + valor
    conta = conta + 1

media = total / conta
print ('Média:', media)

# agora utilizando lista
numlist = list()
while (True):
    inp = input('Digite um número: ')
    if inp == 'n': break
    valor = float(inp)
    numlist.append(valor)   #APPEND: adciona o número no final da lista

media = sum(numlist) / len(numlist)
print('Média: ',media)

ingrediente = ['calabresa', 'parmesão', 'champion']

if 'calabresa' in ingrediente:
	print('adicione calabresa')
if 'mussarela' in ingrediente:
	print('adicione mussarela')
if 'champion' in ingrediente:
	print('adicione champion')
'''
# Começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados 
unconfirmed_users = ['alice', 'brian', 'candace', 'joão', 'ester']
confirmed_users = []
# Verifica cada usuário até que não haja mais usuários não confirmados 
#Transfere cada usuário verificado para a lista de usuários confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verificando usuário: " + current_user.title()) 
    confirmed_users.append(current_user)
# Exibe todos os usuários confirmados 
print("\nOs seguintes usuários foram confirmados:") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []