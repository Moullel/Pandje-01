preco_pizza = float(input("Qual o preço da pizza? R$ "))
quantidade_pizzas = float(input("Quantas pizzas foram vendidas no mês? "))
Faturamento_bruto = preco_pizza * quantidade_pizzas

custos_fixos = Faturamento_bruto *0.30
custos_variaveis = Faturamento_bruto *0.20

#calculo de faturamento líquido
faturamento_liquido=faturamento_liquido = Faturamento_bruto - (custos_fixos + custos_variaveis)

print(f"\nFaturamento bruto: R$ {Faturamento_bruto:.2f}")
print(f"a) Custos fixos: R$ {custos_fixos:.2f}")
print(f"b) Custos variáveis: R$ {custos_variaveis:.2f}")
print(f"c) Faturamento líquido: R$ {faturamento_liquido:.2f}")
