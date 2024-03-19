def qartefacto(artefacto):
  if artefacto == "tesoro o decorativo":
      return "Es un tesoro."
  else:
      return "Es un adorno decorativo."

def main():
  print("Los jóvenes aventureros han encontrado un artefacto en la Ciudad Encantada.")
  artefacto = input("Describa el artefacto encontrado: ")

  resultado = qartefacto(artefacto)
  print(resultado)

if __name__ == "__main__":
  main()
