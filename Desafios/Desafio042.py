r1 = float(input("Digite o valor da primeira reta: "))
r2 = float(input("Digite o valor da segunda reta: "))
r3 = float(input("Digite o valor da terceira reta: "))
if r1 == r2 and r1 == r3 and r2 == r3:
    print ("É um triângulo equilátero!")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("É um triângulo é isósceles!")
elif r1 != r2 and r1 != r3 and r2 != r3:
    print("É um triângulo é escaleno!")

