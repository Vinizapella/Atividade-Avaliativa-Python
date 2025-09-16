try:
  arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError:
  print("Erro: Arquivo não encontrado.")
finally:
  print("Fim do bloco try-except")