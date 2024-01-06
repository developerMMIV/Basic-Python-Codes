import math
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co**2 + ca**2)**(1/2)
print('A hipotenusa vai pedir {:.2f}'.format(hi))'''

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjancente:'))
hi = math.hypot(co,ca)
print('A hypotenusa vai pedir {:.2f}'.format(hi))
