# Entrada de dados
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

# Cálculo do salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Cálculo dos descontos
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

# Cálculo do salário líquido
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Saída
print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"a) Pago ao IR: R$ {ir:.2f}")
print(f"b) Pago ao INSS: R$ {inss:.2f}")
print(f"c) Pago ao sindicato: R$ {sindicato:.2f}")
print(f"d) Salário líquido: R$ {salario_liquido:.2f}")