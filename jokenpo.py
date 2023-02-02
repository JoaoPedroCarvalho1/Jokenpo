from random import randint
from time import sleep
itens=('pedra','papel','tesoura')
computador=randint(0,2)
print('''suas opções 
[0] Pedra
[1] Tesoura
[2] Papel''')
jogador=int(input('Qual sua jogada?'))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('po!!!')
print('-='*10)
print('computador jogou {}.'.format(itens[computador]))
print('jogador jogou {}.'.format(itens[jogador]))
print('-='*10)
if computador == 0:
	if jogador ==0:
		print('empate')
	elif jogador ==1:
		print('Computador ganhou')
	elif jogador ==2:
		print('jogador ganhou')
	else :
		print('jogada inválida')
elif computador == 1:
	if jogador == 0:
		print('jogador ganhou')
	elif jogador == 1:
		print('empate')
	elif jogador == 2:
		print('Computador ganhou')
	else:
		print('jogada inválida')
elif computador == 2:
	if jogador == 0:
		print('Computador ganhou')
	elif jogador ==1:
		print('jogador ganhou')
	elif jogador == 2:
		print('empate')
	else:
		print('jogada inválida')