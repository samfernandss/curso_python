"""
Todo tipo de dado recebido com input() entra como string
Pra tratar como número, é necessário fazer cast
"""
print("qual seu nome?")
nome = input()

print("Qual sua idade?")
idade = input()

print("Seja bem vindx, " + nome + ", de " + idade + " anos de idade!")
print('Fazendo de um jeito diferente, viu %s de %s anos' % (nome, idade))

#moderno
print('Seja bem vindx, {0}'.format(nome));
print(f'Prazer em conhecê-lx, {nome}, em seus plenos {idade} anos.')