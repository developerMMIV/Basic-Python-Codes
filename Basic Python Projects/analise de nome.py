n = str(input('Digite o seu nome completo:')).strip()
nome= n.split()
print("Prazer te conhecer {}".format(n))
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[-1]))
print("o seu nome em maicusulo é {}".format(n.upper()))
print("O seu nome em minusclulo é {}".format(n.lower()))
print("as letras o seu nome tem é {}  ".format(len(n)))
print("O seu nome começa com 'A' ? : {}".format(n[:5].upper()=="A"))
print("E termina com O?: {} ".format(n[-1].upper()=="O"))
print("Tem a letra 'c'?: {}".format(n.count("c")))
print("Se as letras do seu nome fosse contado em X2, vai ser assim:{} ".format(n[0::2]))

#if nome

