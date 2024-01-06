salario = float(input("Qual é o seu salario atual?: R$"))

if salario<=1250:
    novo = salario+ (salario*15/100)
else:
    novo = salario+(salario*10/100)
print("Quem ganhava R${} vai ganhar um aumento de R${}".format(salario,novo))