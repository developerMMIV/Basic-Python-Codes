from random import  choice
n1 = input("Primero aluno:")
n2 = input("segundo aluno:")
n3 = input("Terceiro aluno:")
n4 = input("Quarto aluno:")
lista = [n1,n2,n3,n4]
escohlido = choice(lista)

print("O aluno escohido foi {}".format(escohlido))

