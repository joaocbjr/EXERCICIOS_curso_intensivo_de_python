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
'''


