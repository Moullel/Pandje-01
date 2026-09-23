def pedir_numeros():
    while True:
        try:
            num_int1 = int(input("Digite o primeiro numero INTEIRO: "))
            break
        except ValueError:
            print("ERRO! Digite um numero válido")

    while True:
        try:
            num_int2 = int(input("Digite o segundo numero INTEIRO: "))
            break
        except ValueError:
            print("ERRO! Digite um numero válido")

    while True:
        try:
            num_real = float(input("Digite um número REAl (use ponto para decimais): "))
            break
        except ValueError:
            print("Erro! Digite um numero válido.")

    return num_int1,num_int2,num_real

inteiro1,inteiro2,real = pedir_numeros()

print("\n--- Valores digitados com sucesso! ---")
print(f"Primeiro inteiro: {inteiro1} (Tipo:{type(inteiro1).__name__})")
print(f"Segundo inteiro: {inteiro2} (Tipo:{type(inteiro2).__name__})")
print(f"Numero Real : {real} (Tipo:{type(real).__name__})")

print("Letra a - ", inteiro1*2 * inteiro2/2)
print("letra b - ", inteiro1*3 + real)
print("letra c - ", real**3)
