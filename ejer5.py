def main():
  print("¡Bienvenido!")
  potencia_hechizo = int(input("Ingrese la potencia del hechizo: "))
  resistencia = float(input("Ingrese el nivel de resistencia del enemigo: "))
  resultado = potencia_hechizo + resistencia
  print("El resultado de la suma de la potencia del hechizo y la resistencia del enemigo es:", resultado)

if __name__ == "__main__":
  main()