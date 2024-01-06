print('='*20)
print("Analisador de triangulos")
print("="*20)
r1 = float(input("Digite o primeiro codigo:"))
r2 = float(input("Digite o segundo codigo:"))
r3 =float(input("Digite o terceiro codigo"))
if r1 <r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("O segmentos PODEM FORMAR Triangulo")
else:
    print("Os segmentos NAO PODEM FORMAR UM SEGMENTO")
