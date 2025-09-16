def contar_vogais(texto):
  vogais = "aeiouAEIOU"
  total_vogais = 0
  for letra in texto:
    if letra in vogais:
      total_vogais += 1
  return total_vogais
print(f"A frase 'Ola Mundo' tem {contar_vogais('Ola Mundo')} vogais.")