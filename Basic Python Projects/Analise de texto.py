nome = str(input("Digite o seu nome completo:")).strip()
print(" Analisando o seu nome........")
print("o seu nome Maiuscula é:{}".format(nome.upper()))
print("o seu nome minusclula é :{}".format(nome.lower()))
print("o primeiro letra do seu nome é {}".format(nome[0]))
print("e o ultimo:{}".format(nome[len(nome)-1]))
print("O seu nome tem {} letras,e ".format(len(nome) - nome.count(" ")))
print("O primeiro nome tem {} letras".format(nome.find(' ')))
#print(" se eu trocar o seu ")