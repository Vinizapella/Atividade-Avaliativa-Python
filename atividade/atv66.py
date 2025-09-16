def is_palindrome(texto):
  texto_formatado = texto.replace(" ", "").lower()
  return texto_formatado == texto_formatado[::-1]

print(f"'Ovo' é palíndromo? {is_palindrome('Ovo')}")
print(f"'A sacada da casa' é palíndromo? {is_palindrome('A sacada da casa')}")
print(f"'Casa' é palíndromo? {is_palindrome('Casa')}")