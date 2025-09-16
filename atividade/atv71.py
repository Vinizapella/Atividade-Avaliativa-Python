def unir_listas(lista1, lista2):
  return list(set(lista1 + lista2))

nomes1 = ["Ana", "Carlos", "Bia"]
nomes2 = ["Carlos", "Daniel", "Ana"]
lista_final = unir_listas(nomes1, nomes2)
print(f"{lista_final}")