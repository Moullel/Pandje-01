altura = float(input("Informe a sua altura: "))
peso = float(input("Informe o seu peso: "))

imc = peso / (altura**2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
        print("ta pasando fome")
elif 18.5 <= imc < 25:
        print("Peso Normal")
elif 25 <= imc < 30:
        print("Ta gordo")
else:
        print("Eu conheço 10 gordos e você  é 5 deles")

