def fibonacci(n):
  a, b = 0, 1
  sequencia = []
  while a <= n:
    sequencia.append(a)
    a, b = b, a + b
  return sequencia
print(fibonacci(50))