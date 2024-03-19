def calcular_fac(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * calcular_fac(n - 1)

def combi(n, k):
  if k > n:
      return 0
  else:
      return calcular_fac(n) / (calcular_fac(k) * calcular_fac(n - k))

n_personajes = 10
k_equipo = 3

resultado = combi(n_personajes, k_equipo)
print("La combinación de", n_personajes, "elementos tomados de", k_equipo, "es", resultado)