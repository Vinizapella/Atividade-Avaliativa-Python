def encontrar_menor(lista_numeros):
  if not lista_numeros:
    return None
  return min(lista_numeros)

numeros = [25, 8, 42, -5, 12]
menor = encontrar_menor(numeros)
print(f"{menor}")