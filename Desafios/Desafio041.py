ano_atual = 2023
ano = int(input("Digite o ano de nascimento do atleta:"))
calc_ano = ano_atual - ano
if calc_ano <= 9:
    print("Categoria mirim!")
elif calc_ano > 9 and calc_ano <= 14:
    print("Categoria infantil!")
elif calc_ano > 14 and calc_ano <= 19:
    print("Categoria junior!")
elif calc_ano == 20:
    print("Categoria sênior!")
else:
    print("Categoria master!")