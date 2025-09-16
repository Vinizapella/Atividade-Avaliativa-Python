def inverter_dicionario(dicionario):
  return {valor: chave for chave, valor in dicionario.items()}

capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago"}
paises = inverter_dicionario(capitais)
print(f"{paises}")