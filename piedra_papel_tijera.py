print('Bienvenidos al famoso juego "PIEDRA, PAPEL O TIJERA"')

nombre1 = input('Por favor, ingrese el nombre el jugador 1: ')
nombre2 = input('Por favor, ingrese el nombre el jugador 2: ')

jugar = True

while jugar:
    jugador1 = input(nombre1 + ', ingrese su elección: piedra, papel o tijera: ').upper()
    jugador2 = input(nombre2 + ', ingrese su elección: piedra, papel o tijera: ').upper()

    condicion1 = jugador1 == 'PIEDRA' and jugador2 == 'TIJERA'
    condicion2 = jugador1 == 'PAPEL' and jugador2 == 'PIEDRA'
    condicion3 = jugador1 == 'TIJERA' and jugador2 == 'PAPEL'

    if jugador1 == jugador2:
        print("El resultado fue un empate!")
    else:
        if condicion1 or condicion2 or condicion3:
            print('Felicitaciones '+nombre1+', ganaste el juego!')
        else:
            print('Felicitaciones '+nombre2+', ganaste el juego!')
            
    respuesta = input('Quieren jugar de nuevo? S/N: ').lower()  

    if respuesta == 'n':
        jugar = False
        print('Muchas gracias por participar! Hasta luego!')