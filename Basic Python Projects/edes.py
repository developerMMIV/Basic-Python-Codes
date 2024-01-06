preço = float(input('qual é o preço de produto?, R$:'))
novo = preço - (preço*5/100)
print('O produto que custava R${:.2f} na promoçao com desconto de 5%, vai custar {:.2f} '.format(preço,novo))

