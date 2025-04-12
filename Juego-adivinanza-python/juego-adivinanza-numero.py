import random

def juego_adivinanza():
    #generar un numero del 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanzas")
    print("Debes adivinar un numero entero entre 1 y 100")
    print("Intenta adivinar")

    while not adivinado:
        #solicitar un numero del 1 al 100
        adivinanza = input("introduzaca un numero del 1 al 100 >>>")

        #verficar que la entrada sea un numero

        if(adivinanza.isdigit()):
            adivinanza = int(adivinanza)# aqui lo pasamos de tecto a entero
            intentos +=1

            if adivinanza < numero_secreto:
                print("El numero igresado es menor que el numero secreto")
            elif adivinanza > numero_secreto:
                print("El numero igresado es mayor que el numero secreto")
            else:
                print(f"Felicitaciones has ganado! El numero ingresado {adivinanza} es el numero secreto y lo lograste en {intentos}")
        else:
            print("Por favor introduzca un numero valido entre 1 y 100")

juego_adivinanza()


