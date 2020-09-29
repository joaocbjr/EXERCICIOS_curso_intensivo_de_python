print()
print(
    '6.3 – Glossário:\n'
    ' Um dicionário Python pode ser usado para modelar um '
    'dicionário de verdade. No entanto, para evitar confusão, '
    'vamos chamá-lo de glossário.\n'
    ' • Pense em cinco palavras relacionadas à programação '
    'que você conheceu nos capítulos anteriores. Use essas '
    'palavras como chaves em seu glossário e armazene seus '
    'significados como valores.\n'
    ' • Mostre cada palavra e seu significado em uma saída '
    'formatada de modo elegante. Você pode exibir a palavra '
    'seguida de dois-pontos e depois o seu significado, ou '
    'apresentar a palavra em uma linha e então exibir seu '
    'significado indentado em uma segunda linha. Utilize o '
    'caractere de quebrade linha "( \ n )" para inserir uma '
    'linha em branco entre cada par palavra-significado em '
    'sua saída.'
)
print()
print("GLOSSÁRIO:")
glossario_0 = {'verbet': 'if', 'signif': 'altera o fluxo baseado no valor, verdadeiro ou falso, de uma expressão lógica.'}
glossario_1 = {'verbet': 'lista', 'signif': 'é uma coleção de itens em uma ordem em particular.'}
glossario_2 = {'verbet': 'variaveis', 'signif': 'é convencionalmente, um elemento representante do conjunto de todos os resultados possíveis de um fenômeno.'}
glossario_3 = {'verbet': 'strings', 'signif': 'é simplesmente uma série de caracteres.'}
glossario_4 = {'verbet': 'tupla', 'signif': 'é uma Lista imutável.'}

print(glossario_0['verbet'].title() + ': ' + glossario_0['signif'])
print(glossario_1['verbet'].title() + ': ' + glossario_1['signif'])
print(glossario_2['verbet'].title() + ': ' + glossario_2['signif'])
print(glossario_3['verbet'].title() + ': ' + glossario_3['signif'])
print(glossario_4['verbet'].title() + ': ' + glossario_4['signif'])