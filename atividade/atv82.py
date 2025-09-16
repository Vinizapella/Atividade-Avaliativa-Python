def somar_pares(lista):
  soma = 0
  for numero in lista:
    if numero % 2 == 0:
      soma += numero
  return soma

numeros_soma = [1, 2, 3, 4, 5, 6, 7, 8]
soma_dos_pares = somar_pares(numeros_soma)
print(f"{soma_dos_pares}")