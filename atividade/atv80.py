def subconjunto(conjunto1, conjunto2):
  return conjunto1.issubset(conjunto2)

set_e = {10, 20}
set_f = {10, 20, 30, 40}
print(f"{subconjunto(set_e, set_f)}")