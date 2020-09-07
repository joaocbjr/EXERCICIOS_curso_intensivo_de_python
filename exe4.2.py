print()
print('4.2 – Animais:\n Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, então, utilize um laço for para exibir o nome de cada animal.\n•  Modifique  seu  programa  para  exibir  uma  frase  sobre  cada  animal,  por exemplo, Um cachorro seria um ótimo animal de estimação.\n•  Acrescente  uma  linha  no  final  de  seu  programa  informando  o  que  esses animais têm em comum. Você poderia exibir uma frase como Qualquer  um desses animais seria um ótimo animal de estimação!')
print()

animais = ['cachorro', 'gato', 'gambá']

print('Os animais são:')
for animal in animais:
    print(animal)

print('O ' + animais[0] + ' é um bom companheiro.')
print('Quem tem uns peidos fedorentos é o ' + animais[2])
print('Aqui em casa não tem mais ' + animais[1] + ' na energia')
print()
print('Todos esses animais são mamiferos')
print('esse arquivo vai ser versionado')