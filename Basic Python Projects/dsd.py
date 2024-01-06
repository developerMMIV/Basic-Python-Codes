larg = float(input('Digite a largura do seu parede:'))
altr =  float(input('Digite a altura do seu parede:'))

area = larg * altr

print('Sua parede tem a dimensão de {} x {} e sua area é de {}m².'.format(larg,altr,area))
tinta = area / 2
while tinta <= 25:
   print('Sua parede é pequeno, {}l nao é sufficiente para pintar  mais que 50m² de parede ')
   larg = float(input("Digite de novo, largura:"))
   altr = float(input("altura:"))
   area = larg * altr
   tinta = area / 2

else:
    print('para pinta esssa parede, voce precisara de {}l de tinta.'.format(tinta))


