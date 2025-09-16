def diferenca_conjuntos(conjunto1, conjunto2):
  return conjunto1.difference(conjunto2)

set_c = {1, 2, 3, 4, 5}
set_d = {4, 5, 6, 7}
diferenca = diferenca_conjuntos(set_c, set_d)
print(f"{diferenca}")