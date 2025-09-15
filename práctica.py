
import random

print("Bienvenido al juego!")

jugar = True

while jugar:
    numero_a_adivinar = random.randint(0,100)
    numero_elegido = int(input('Por favor, elige un número del 0 al 99: '))
    
    while numero_elegido != numero_a_adivinar:
        if numero_elegido < numero_a_adivinar:
            print('No has acertado! El número a adivinar es mayor al número que elegiste')
            numero_elegido = int(input('Por favor, elige otro número: '))
        else:
            print('No has acertado! El número a adivinar es menor al número que elegiste')
            numero_elegido = int(input('Por favor, elige otro número: '))
        
    respuesta = input("Felicitaciones, acertaste el número! Querés jugar de nuevo? \n S para si y N para no: ")
    if respuesta == 's':
        jugar = True
        
    else:
        jugar = False
        print('MUchas gracias por participar! Hasta luego!')
