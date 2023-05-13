nome = str(input("Qual é o seu nome?"))
if nome == "Lucas":
    print("Que nome bonito!")
elif nome == "Lucas" or nome == "Gustavo" or nome == "Gabriel":
    print ("seu nome é bem popular no Brasil!")
else:
    print("Seu nome é bem normal!")
print ("Tenha um ótimo dia, {}!".format(nome))