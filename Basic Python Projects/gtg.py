salario = float(input("Qual é o salario atual do funcionairo? R$"))
novo = salario + (salario * 15/ 100)
alt = salario * 15/100
print(" Um funcionario que ganhava R${:.2f}, com aumento de 15% ou R${:.2f}, ele ganha R${:.2f} "
      .format(salario,alt,novo))
