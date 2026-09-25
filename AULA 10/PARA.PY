# for i in range(10):
#     print("Oi você!")
# cont= 0
# while cont<=9:
#     print("Oi você!")
#     cont+=1    


# for i in range(10):
#     print(i)
# for i in range(5):
#     print(i) 

# for i in range(2,8):
#     print(i)       

# for i in range(0,11,2):
# #     print(i)    

# for i in range(10,0,-1):
#     print(i)    

# A= int(input("Insira um numero inteiro:")) 
# B= int(input("insira um outro numero inteiro:"))
# for i in range(A,B+1):
#     print(i)




# for i in range(0,22,2):
#      print(i)

# soma=0
# N=int(input("Insira um numero da sua escolha:"))
# for i in range(N+1):
#     soma=soma+i
# print(soma)



# O_NUMERO=int(input("Insira Um numero :"))
# for i in range (11):
    
#     print  (f' {i}x{O_NUMERO}={i*O_NUMERO}') 

# numero=int(input("Digite um numero:"))
# fat = 1
# for i in range(1,numero+1):
#     fat *= i
#   print(f"O fatorial é: ")  



# for i in range(10,0,-1):
#     print(i)
# soma=0
# for i in range(1,51):
#     if i % 2==0:
#         soma+=i
#         print(soma)

# Palavra= input("Digite uma palavra:")
# for letra in Palavra:
#     print(letra)  '      

# frase= input("Digite Uma frase:")
# contador=0
# for letra in frase:
#     if letra != " "  and letra not in "aeiouAEIOU":
#      contador += 1
# print(f"A quantidade de caracteres é:{contador}")



# A=0
# B=1
# for sequência in range(100000):
#     C=A+B
#     print(A)
#     A=B
#     B=C


base=int(input("Digite o valor base:"))
expo=int(input("Digite o expoente"))
resultado=1
for i in range(expo):
    resultado=resultado*base
    print("Resultado:",resultado)
   
   
