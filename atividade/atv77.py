def filtrar_dicionario(dicionario, valor_minimo):
  return {chave: valor for chave, valor in dicionario.items() if valor >= valor_minimo}

notas = {"Ana": 8.5, "Beto": 6.0, "Carla": 9.0, "Daniel": 5.5}
aprovados = filtrar_dicionario(notas, 7.0)
print(f"{aprovados}")