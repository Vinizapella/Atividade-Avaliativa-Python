def substituir_palavra(frase, palavra_antiga, palavra_nova):
  return frase.replace(palavra_antiga, palavra_nova)
frase_original = "O dia está lindo, um lindo dia para programar."
nova_frase = substituir_palavra(frase_original, "lindo", "maravilhoso")
print(nova_frase)