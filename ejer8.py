def clasificar_mensaje(mensaje):
  if "tesoro" in mensaje.lower():
      return "¡Encontraste un tesoro!"
  elif "criatura" in mensaje.lower():
      return "¡Encontraste una criatura!"
  elif "trampa" in mensaje.lower():
      return "¡Cuidado! Es una trampa mortal."
  else:
      return "No se puede determinar la naturaleza del hallazgo."

def main():
  print("Los jóvenes aventureros han encontrado un mensaje.")
  mensaje = input("Describe el mensaje encontrado: ")

  resultado = clasificar_mensaje(mensaje)
  print(resultado)

if __name__ == "__main__":
  main()
