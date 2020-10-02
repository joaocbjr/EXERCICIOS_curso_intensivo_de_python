print('\n6.4 – Glossário 2:\n'
    ' Agora que você já sabe como percorrer um dicionário comum '
    'laço, limpe o código do Exercício 6.3 (página 148), '
    'substituindo sua sequência de instruções print por um laço '
    'que percorra as chaves e os valores do dicionário. Quando '
    'tiver certeza de que seu laço funciona, acrescente mais cinco '
    'termos de Python ao seu glossário. Ao executar seu programa '
    'novamente, essas palavras e significados novos deverão ser '
    'automaticamente incluídos na saída.\n')
print("GLOSSÁRIO:")
glossario = {
    'if': 'altera o fluxo baseado no valor, verdadeiro ou falso, de uma expressão lógica.',
    'lista': 'é uma coleção de itens em uma ordem em particular.',
    'variaveis': 'é convencionalmente, um elemento representante do conjunto de todos os resultados possíveis de um fenômeno.',
    'strings': 'é simplesmente uma série de caracteres.',
    'tupla': 'é uma Lista imutável.'
    }

for verbete, signif in glossario.items():
    print(verbete + ': ' + signif)
