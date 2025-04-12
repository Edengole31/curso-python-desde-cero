import random  # Importa el módulo random para poder elegir una palabra al azar

# Esta función devuelve una palabra secreta elegida al azar de una lista
def obtener_palabra_secreta():
    palabras = ["python", "java", "react", "javajs", "linux", "windows", "angular", "django"]
    return random.choice(palabras)

# Esta función muestra el progreso actual del jugador
# Reemplaza las letras no adivinadas por guiones bajos
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinadas = ''  # Acá se va construyendo la palabra con letras o "_"
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinadas += letra  # Si la letra ya fue adivinada, se muestra
        else:
            adivinadas += '_'   # Si no, se muestra un "_"
    return adivinadas

# Esta es la función principal del juego
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()  # Selecciona la palabra secreta
    letras_adivinadas = []  # Lista para guardar las letras que el jugador ya usó
    intentos = 7  # Intentos disponibles
    juego_terminado = False  # Bandera que indica si el juego terminó

    print("Bienvenidos al juego el ahorcado")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))  # Muestra el estado inicial de la palabra

    # Bucle principal del juego: continúa mientras no termine y haya intentos
    while not juego_terminado and intentos > 0:
        adivinanza = input("Ingrese una letra: ").lower()  # El jugador ingresa una letra

        # Validaciones:
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor ingrese una letra válida")  # Si no es una letra única, se muestra error
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esta letra")  # Si la letra ya se usó, se avisa
        else:
            letras_adivinadas.append(adivinanza)  # Se guarda la letra en la lista

            if adivinanza in palabra_secreta:
                print(f"La letra {adivinanza} se encuentra en la palabra secreta")  # Letra correcta
            else:
                intentos -= 1  # Letra incorrecta, pierde un intento
                print(f"La letra {adivinanza} no se encuentra en la palabra, te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)  # Actualiza el progreso
        print(progreso_actual)

        # Verifica si ya no hay "_" → significa que ganó
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Has ganado! La palabra secreta es: {palabra_secreta}")

    # Si se quedó sin intentos, se pierde el juego
    if intentos == 0:
        print(f"Lo sentimos mucho, la palabra secreta era: {palabra_secreta}")

# Llama a la función principal para iniciar el juego
juego_ahorcado()




