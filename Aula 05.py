cart= str(input("Habilitado:?"))
idade= float(input("Sua idade:?"))
if(cart=="Sim") and (idade>=18):
    print("A Pista é Sua!")

else:
    print("Não Tenha Preça Filho(a)")    
#####################################################################
titulo=str(input("Possui Titulo:?" ))
idade= float(input("Digite a Sua idade?:"))
if(titulo=="Sim"and(idade>=16)):
    print("O Futuro esta nas suas mãos")
else:
    print("Ainda NÃO!!!")    

valor=float(input("Valor das compras?:"))
vip=str(input("È Amigo da viginhança?:" ))
if(valor>=100 or (vip =="S")):
    print("10% Garantidos")
else:
    print("Continue Pobre")    