time = input('informe o nome do time: ')
vitorias = int(input('quantas vitorias: '))
derrotas = int(input('quantas derrotas: '))
empates = int(input('quantas empates: '))

pontosTotais = vitorias * 3 + empates
totalDeJogos = vitorias+derrotas+empates
pontosPerdidos = derrotas*3+empates*2
aproveitamento = pontosTotais / (totalDeJogos * 3) * 100

print('O time do {} jogou um total de {}'.format(time, totalDeJogos), 'jogos')
print('tendo um total de:', vitorias, 'vitorias')
print('tendo um total de:', derrotas, 'derrotas')
print('tendo um total de:', empates, 'empates')
print('total de pontos perdidos', pontosPerdidos)
print('tendo um total de {} pontos'.format(pontosTotais))
print('aproveitamento do time foi: {:.2f}$'.format(aproveitamento))
