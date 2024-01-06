distance  = float(input("Qual é a distancia da sua viagem?: "))
print("voce vai começar uma viagem de {}km ".format(distance))
if distance <= 200:
    preco = distance*0.50
else:
    preco =distance*0.45

print("E o preço da sua passagem vai ser R${} reais ".format(preco))