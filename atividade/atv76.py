def soma_valores(dicionario):
  return sum(dicionario.values())

estoque = {"maçãs": 150, "bananas": 200, "laranjas": 120}
total_itens = soma_valores(estoque)
print(f"{total_itens}")