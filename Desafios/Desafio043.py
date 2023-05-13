peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura(ex: 1.75): "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso ideal!")
elif imc >= 25 and imc < 30:
    print("Você está sobrepeso!")
elif imc >= 30 and imc < 40:
    print("Você está no nível de obesidade!")
else:
    print("Você está com um nível de obesidade morbida!")