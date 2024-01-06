from random import randint
computador = randint(0,5)
print('-=-'*10)
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar')
print("-=-"*10)
Jogador = int(input('Em que numero eu pensei'))
if Jogador == computador:
    print("Parabens, voce ganhou ")
else:
    print("vc perdeu")