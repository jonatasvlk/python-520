
# tipos primitivos
string = 'Jonatas'
inteiro = 24
flutuante = 150000.92
booleano = True

# estrutura de dados
tupla = (1, 2, 3, 4)
lista = [1, 2, 3, 4]
dicionario = {
'nome': 'Jonatas',
'idade': 26
}

print (string)

nome = input('Digite seu nome: ')
print (nome)
idade = input ('digite sua idade:')
print (idade)
email = input ('digite seu email:')
print (email)
sexo = input ('digite seu sexo:')
print (sexo)
altura = input ('digite sua altura:')
print (altura)
peso = input ('digite seu peso:')
print (peso)

usuario = {
	'nome': input ('digite seu nome: '),
	'idade': input ('Digite sua idade: '),
	'email': input ('Digite seu email: '),
	'sexo': input ('Digite seu sexo: '),
	'altura': input ('Digite sua altura: '),
	'peso': input ('Digite seu peso: ')
}
print (usuario)

# ex2: Imprimir no terminal SOMENTE
# o nome e a idade digitas

nome = usuario ['nome']
idade = usuario ['idade']

print(nome, idade)


