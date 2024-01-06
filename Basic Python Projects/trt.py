import math

data = int(input('Digite o valor do seu numero:'))
mint = int(input('Digite o seu numero de novo:'))

iq = math.sqrt(data)/mint * 23

print("Agora, vc esta me devendo ${:.2f} dollares ".format(iq))