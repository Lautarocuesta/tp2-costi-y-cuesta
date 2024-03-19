nompersonaje = input("Ingrese el nombre de su personaje: ")
numpociones = int(input("Ingrese el número de pociones que tiene su personaje: "))

mensaje_descripcion = "Tu personaje " + nompersonaje + " está listo para la aventura. "
mensaje_descripcion += "Posee " + str(numpociones) + " pociones mágicas para enfrentar los desafíos que le esperan."

print(mensaje_descripcion)
