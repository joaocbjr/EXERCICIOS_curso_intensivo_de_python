print()
print('3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto  agora  tem  mais  espaço  disponível.  Pense  em  mais  três  convidados para o jantar.\n* Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescenteuma instrução print  no  final  de  seu  programa  informando  às  pessoas  quevocê encontrou uma mesa de jantar maior.\n* Utilize insert() para adicionar um novo convidado no início de sua lista.\n* Utilize insert() para adicionar um novo convidado no meio de sua lista.\n* Utilize append() para adicionar um novo convidado no final de sua lista.\n* Exiba um novo conjunto de mensagens de convite, uma para cada pessoaque está em sua lista.')
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
convidado.insert(4, 'Dona Chica')
convidado.append('Roberto')

print(mensagem + convidado[1])
print(mensagem + convidado[2])
print(mensagem + convidado[3])
print(mensagem + convidado[4])
print(mensagem + convidado[5])
print(mensagem + convidado[6])