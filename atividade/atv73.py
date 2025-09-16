def dividir_lista(lista_numeros):
  pares = []
  impares = []
  for numero in lista_numeros:
    if numero % 2 == 0:
      pares.append(numero)
    else:
      impares.append(numero)
  return (pares, impares)

numeros_misturados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = dividir_lista(numeros_misturados)
print(f"Pares={pares}, Ímpares={impares}")