def interseccao_conjuntos(conjunto1, conjunto2):
  return conjunto1.intersection(conjunto2)

set_g = {10, 20, 30, 40}
set_h = {30, 40, 50, 60}
intersecao = interseccao_conjuntos(set_g, set_h)
print(f"{intersecao}")