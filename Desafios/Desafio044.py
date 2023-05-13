print("À vista ou cheque: 1")
print ("À vista no cartão: 2")
print("Em até duas vezes no cartão de crédito: 3")
print("Em 3 vezes ou mais no cartão de crédito: 4")
forma_de_pagamento = int(input("Digite o número da forma de pagamento desejada:"))
vp = float(input("Digite o valor do produto:"))
vporc = vp / 100
if forma_de_pagamento == 1:
    valor_desc_10 = vporc * 10
    valor_descontado = vp - valor_desc_10
    print("O valor do seu produto com essa forma de pagamento será de: {}".format(valor_descontado))
elif forma_de_pagamento == 2:
    valor_desc_5 = vporc* 5
    valor_descontado2 = vp - valor_desc_5
    print("O valor do seu produto com essa forma de pagamento será de: {}".format(valor_descontado2))
elif forma_de_pagamento == 3:
    print("O valor do seu produto será de: {}".format(vporc))
elif forma_de_pagamento == 4:
    juros = vporc * 20
    juros_adc = (vp + juros)
    print("O valor do seu produtor com essa forma de pagamento será de: {}".format(juros_adc))