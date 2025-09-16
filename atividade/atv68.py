def invertido(frase):
  palavras = frase.split(' ')
  palavras_invertidas = [palavra[::-1] for palavra in palavras]
  return ' '.join(palavras_invertidas)
print(invertido("Python é legal"))