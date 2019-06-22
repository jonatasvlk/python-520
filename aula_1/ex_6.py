
def receber_inteiro(mensagem):
	valor = input (mensagem)
	if valor.isnumeric():
		return valor
	print('Número invalido')
	exit ()

def receber_inteiro_2(mensagem):
	valor = ''
	while not valor.isnumeric():
		valor = input(mensagem)
	return int(valor)

usuario = {
	'nome' : input('Digite seu nome: '),
	'idade': receber_inteiro_2('Digite sua idade: '),
	'peso' : receber_inteiro_2('Digite seu peso: ')
}		

print(usuario)
	
