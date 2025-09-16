lista_de_compras = [
    ["maçã", 2.50],
    ["arroz", 15.00],
    ["leite", 4.25],
    ["pão", 5.50]
]

total_gasto = 0
for item in lista_de_compras:
  total_gasto += item[1]

print(f"O total gasto foi de R$ {total_gasto:.2f}")