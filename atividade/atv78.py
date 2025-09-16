def unir_conjuntos(conjunto1, conjunto2):
  return conjunto1.union(conjunto2)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
uniao = unir_conjuntos(set_a, set_b)
print(f"{uniao}")