print()
print('4.8 – Cubos:\n Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.')
print()
cubo = []
for value in range(1,11):
    cub = value**3
    cubo.append(cub)
print(cubo)