print("Bem-vindo ao programa de empréstimo bancário para o financiamento da sua casa!")
vcasa = float(input("Digite o valor da casa:"))
vsalario = float(input("Digite o seu salário?:"))
qanos = int(input("Digite em quantos anos deseja pagar esta casa:"))
ano = 12
anos = qanos * ano
prestacao = vcasa / anos
porc_salario = vsalario / 100
trinta_porc_salario = porc_salario * 30
if prestacao >= trinta_porc_salario:
    print ("Empréstimo negado!")
else:
    print ("Empréstimo confirmado!")