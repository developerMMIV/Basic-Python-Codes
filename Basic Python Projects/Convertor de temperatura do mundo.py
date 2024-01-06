sao_paulo = float(input('Digite a temperatura em sao paulo:'))
rio_de_janeiro = float(input('Digite a temperatura em Rio de Janeiro:'))
london = float(input('Digite a temperatura em London:'))
curitiba = float(input('Digite a temperatura em curitiba:'))

f = ((9*sao_paulo)/5)+ 32
f2 = ((9*rio_de_janeiro)/5)+32
f3 = ((9*london)/5)+32
f4 = ((curitiba*9)/5)+ 32

print('A Temperatura:')
print(' Em Sao paulo tem {}ºc , {}ºf '.format(sao_paulo,f))
print(' Em Rio de Janeiro tem {}ºc , {}ºf '.format(rio_de_janeiro,f2))
print(' Em London tem {}ºc , {}ºf '.format(london,f3))
print(' Em Curitiba tem {}ºc , {}ºf '.format(curitiba,f4))

