login=input("Digite seu login: ")
password=input("Digite sua senha: ")
print(f"Login: {login}")
print(f"Senha: {password}")

if login=="Moullel" and password=="123456":
    print("Bem vindo ao sistema!")
else:
    print("Login ou senha incorretos. Tente novamente.")
    exit()
