import random

adivinanzas = {
    "¿Qué cosa se puede ver con los ojos cerrados?": "sueños",
    "Blanco por dentro, verde por fuera, si quieres que te lo diga espera.": "pera",
    "No tiene patas, ni garras, ni colmillos y huye al sol más caluroso.": "vampiro"
}

def agregaradivinanzas():
    novoadivinanza = input("Ingresa una nueva adivinanza: ")
    novorespuesta = input("Ingresa la respuesta de la adivinanza: ")

    adivinanzas[novoadivinanza] = novorespuesta
    print("¡La nueva adivinanza ha sido agregada con éxito!")

def jugaradivinanza():
    adivinanza = random.choice(list(adivinanzas.keys()))
    respuesta_correcta = adivinanzas[adivinanza]

    print("¡Juego de Adivinanzas!")
    print("Siguiente adivinanza:")
    print(adivinanza)
    respuesta_usuario = input("¿Cuál es tu respuesta?: ").lower()

    # Verificar si la respuesta es correcta
    if respuesta_usuario == respuesta_correcta:
        print("¡Respuesta correcta! ¡Has avanzado en tu búsqueda del tesoro perdido!")
    else:
        print("Respuesta incorrecta. ¡Sigue intentando!")

def main():
    while True:
        print("\n1. Jugar al Desafío de Adivinanzas")
        print("2. Agregar nueva adivinanza")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugaradivinanza()
        elif opcion == "2":
            agregaradivinanzas()
        elif opcion == "3":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
