ano_atual = 2023
ano = int(input("Digite o seu ano de nascimento:"))
calc_ano = ano_atual - ano
ano_alist = 18 - calc_ano
maiorq_ano_alist = calc_ano - 18
if calc_ano < 18:
    print("Ainda não é a sua hora de se alistar. Ainda falta(m) um total de {}ano(s)!".format(ano_alist))
elif calc_ano == 18:
    print("Já está na hora, você deve se alistar!")
else:
    print("Já passou o seu tempo de alistamento. Se passaram um total de {} ano(s) do seu ano de alistamento!".format(maiorq_ano_alist))