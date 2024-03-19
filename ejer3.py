def factorial(n):
  """Calcula el factorial de un número."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


def calcular_combinaciones(n, r):
  """
  Calcula el número de combinaciones posibles de elegir r elementos de un conjunto de n elementos.
  Utiliza la fórmula C(n, r) = n! / (r! * (n - r)!).
  """
  if r > n:
    return 0
  else:
    return factorial(n) // (factorial(r) * factorial(n - r))


total_personas = int(input("Ingrese el número total de personas: "))
tamano_equipo = int(input("Ingrese el tamaño del equipo: "))
combinaciones = calcular_combinaciones(total_personas, tamano_equipo)
print(f"Se pueden formar {combinaciones} equipos diferentes.")
