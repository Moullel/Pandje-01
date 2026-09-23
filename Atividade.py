v1=str(input("O blindado esta disponivel?: " ))
v2=str(input("A Ponte esta Intacta?:  "))

v3 = input('mascara de gas: ')
v4 = input('Cartão de acesso: ')




if v1 == "SIM" and v2 == "SIM":
    print('A ponte promete ')
elif v3 == 'SIM' and v4 == 'SIM':
    print('Traçar rota pelo Tunel Subterrâneo.')
else:
    print("A ponte promete.") 

