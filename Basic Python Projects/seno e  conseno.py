import math
an = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(an))
print("O angulo de {} tem o Seno de {:.2f}".format(an,seno))
cosseno = math.cos(math.radians(an))
print("O angulo de {} tem o Cosseno de {:.2f}".format(an,cosseno))
tangente = math.tan(math.radians(an))
print("O Angulo de {} tem o Tangente de {:.2f}".format(an,tangente))


