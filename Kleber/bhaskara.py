import math
a = int(input())
b = int(input())
c = int(input())
delta = b**2-4*a*c
print("Delta é igual a: ",delta)
if delta < 0:
    print("Raiz negativa, ERRO!!!")
elif delta == 0:
    x = -b / (2*a)
    print ("Raiz real de x =", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("A raiz de x¹ é: ",x1)
    print("A raiz de x² é: ",x2)
    