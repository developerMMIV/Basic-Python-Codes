print("Bem-Vindo a sacanagem da Joseane!, nos vamos aumentar o seu salario a partir de 10%. "
      "coloque o seu salario para o governo ver como a joseline é uma gopista!")
#print("======================================================================")
salario = int(input('Qual é o seu salario atual? R$  '))

while salario < 1000:
    print('Faz o L ')
    salario = int(input('Qual é o seu salario atual? R$'))
if salario < 2000:
    alt1 = salario * 20/100
    novo = salario + (alt1)
    print('Se vc faz um pix de R$1000, a joseane vai fazer um aumentada com o seu salario atual de R${:.2f},'
          ' de 20% ou seja R${:.2f} e vc  nao vai receber R${:.2f} , mas R${:.2f} '
          .format(salario,alt1,novo,salario - 1000))

elif salario < 3000:
    alt2 = salario * 17.7/100
    novo = salario + alt2
    print('Se vc faz um pix de R$2000, a joseane vai fazer um aumentada com o seu salario atual de R${:.2f},'
          ' de 17.7% ou seja R${:.2f} e vc nao vai receber R${:.2f} , mas R${:.2f} '
          .format(salario, alt2, novo, salario - 2000))

elif salario < 5000:
    alt3 = salario * 15/100
    novo = salario + alt3
    print('Se vc faz um pix de R$3000, a joseane vai fazer um aumentada com o seu salario atual de R${:.2f},'
          ' de 15% ou seja R${:.2f} e vc nao vai receber R${:.2f} , mas R${:.2f} '
          .format(salario, alt3, novo, salario - 3000))
elif salario < 7500:
    alt4 = salario * 12.5/100
    novo = salario + alt4
    print('Se vc faz um pix de R$3000, a joseline vai fazer um aumentada com o seu salario atual de R${:.2f},'
          ' de 15% ou seja R${:.2f} e vc nao vai receber R${:.2f} , mas R${:.2f} '
          .format(salario, alt4, novo, salario - 3000))
elif salario < 10001:
    alt5= salario * 10/100
    novo = salario + alt5
    print("JOSEANE, SEU GOSPISTA FILHA DA P***")
    print('Se vc faz um pix de R$7500, a joseline vai fazer um aumentada com o seu salario atual de R${:.2f},'
          ' de 10% ou seja R${:.2f} e vc nao vai receber R${:.2f} , mas R${:.2f} '
          .format(salario, alt5, novo, salario - 7500))

print("Joseane que dia eu vou pra sua casa pra visitar?")