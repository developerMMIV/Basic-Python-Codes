from random import randint
print("Bem-Vindo ao jogo de marce, para ganhar o dinheiro que o panel vai mostrar, o numero precisa ser no mesmo familiha do numero que o "
      "sistema vai dar (Par). voce so tem tres tentativas e o minimo voce pode colocar é so R$10 reais.  ")
money = int(input("R$"))

while money < 100:
    print("valor não permitido ou nao é par")
    money = int(input("Coloce outro valor: R$"))
if money%2==0:
    print("Se voce peder 3 vezes o seu dinheiro vai pra casa do caralho!")

while not money%2 ==0:
    print("valor não permitido ou nao é par")
    money = int(input("Coloce o seu valor"))
#else:
    #print("Se voce peder 3 vezes o seu dinheiro vai pra casa do caralho")

num = randint(3,5000)+2

if num%2==0:
    print("R${} e R${} é no mesmo familia. parabens!".format(num,money))
else:
    print("R${} e R${} nao é na mesma familha".format(num,money))
