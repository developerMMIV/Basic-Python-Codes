velocidade = float(input('Qual é a velociade atual do carro ? '))

if velocidade >= 80:
    valor = (velocidade-80)*7
    print("Opa, voce passou o limite que é 80km/h mas vc esta indo por {}km/h. agora voce vai pagar R${} ".format(velocidade,valor))

else:
    print('tenha um bom dia e dirija com segurança')