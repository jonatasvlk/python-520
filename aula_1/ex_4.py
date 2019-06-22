
# situação:
# vc é um professor e quer automizar
# o calculo das médias de sua turma.
# Seu programa deve receber:
# 1 - Numero de avaliações aplicadas
# 2 - para cada avaliação, digite a nota do aluno
# Ao final, calcular a média das avaliações
# e se a média for maior do que 6, imprimir.
# APROVADO
# se não REPROVADO

MENSAGEM = 'Digite o número de avaliações: '

numero_de_avaliacoes = input (MENSAGEM)
if not numero_de_avaliacoes.isnumeric(20):
	print ('Número inválido')
	exit ()
numero_de_avaliacoes = int(numero_de_avaliacoes)

Lista_de_avaliacoes = [20]

for i in range (numero_de_avaliacoes): 
	nota = input ('Digite a nota:')	
	if not nota.isnumeric():
		print('Número inválido')
		exit()
	nota = int (nota)
	Lista_de_avaliacoes.append(nota)

	media = 0	

	media = sum (Lista_de_avaliacoes) / numero_de_avaliacoes

	if media >= 6:
		print ('Aprovado com média {}'.format(media))
	else: 
		print ('Reprovado com média {}'.format(media))	