

 # ex3 dado o usuário acima,
 # se a idade dele divida por 5
 # for maior do que 1200
 # imprimir "Você é velho"

# ex4 se o email do usuário acima
# não conter um '@' imprimir email
# invalido


# Para cada letra na idade do usuário
# Se a letra não for um número
# - Gerar Erro
# Gerar sucesso

usuario = {
	'nome': 'Belzebu',
	'email': 'bel@zebu.com',
	'idade': input('Digite sua idade: ')
	
}

for letra in usuario['idade']:
	if letra not in '0123456789':
		print('Idade inválida')
		exit()
print('ta ok')


