from random import randint

Bim = float(input("Bem vindo do jogo da sorte. pra ganhar, os cinco numeros precisa ser pares pra ganhar R$1,000,000, senão, vc perde: R$"))

while Bim <=20:
    print("Valor Baixo para esse jogo")
    Bim = float(input("Coloca outro valor mais de R$20: R$"))
else:
    print("vc pode jogar 3 vezes")





num = randint(1,1000)
num2 = randint(1,1000)
num3 = randint(1 , 1000)
num4 = randint(1,1000)
num5 = randint(1 ,1000)


if num% 2 == 0 and num2%2==0 and num3%2==0 and num4%2 == 0 and num5%2==0:
    print("Os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {} VC GANHOU".format(num,num2,num3,num4,num5))


else:
    print("VC PERDEU. os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {} ".format(num,num2,num3,num4,num5))

    input("Tenta de novo pela segunda vez:")

    num = randint(1,1000)
    num2 = randint(1,1000)
    num3 = randint(1 , 1000)
    num4 = randint(1,1000)
    num5 = randint(1 ,1000)

    if num % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0 and num4 % 2 == 0 and num5 % 2 == 0:
      print("Os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {}. VC GANHOU".format(num, num2, num3,num4, num5))



    else:
      print("VC PERDEU. os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {} ".format(num, num2,num3,num4 ,num5))

      input("Tenta de novo pela terceira vez:")

      num = randint(1, 1000)
      num2 = randint(1, 1000)
      num3 = randint(1, 1000)
      num4 = randint(1, 1000)
      num5 = randint(1, 1000)

      if num % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0 and num4 % 2 == 0 and num5 % 2 == 0:
          print("Os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {}. VC GANHOU".format(num, num2, num3, num4, num5))



      else:
          print("VC PERDEU. os resultados: o primeiro:{}, o segundo:{}, o terceiro:{}, o quarto:{} e o cinco: {} ".format(num, num2, num3, num4, num5))

          print("Vc é um otario exatamente como o pedro.")





