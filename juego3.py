from random import randrange

def juego3():
    print('+-----------------------------------------+')
    print('|             JUEGO DEL DADO              |')
    print('+-----------------------------------------+')
    computadora = 0
    jugador = 0
    while True:
                
        print('+-----------------------------------------+')
        print('|               RESULTADO                 |')
        print('+-----------------------------------------+')
        print(f'|    JUGADOR {jugador}   |   COMPUTADORA {computadora}        |')
        print('+-----------------------------------------+')
        print('+-----------------------------------------+')
        print('| (1)-Tirar Dados                         |') 
        print('| (2)-Salir                               |')
        print('+-----------------------------------------+')
        print()
        
        menu = int(input('Elige una opcion: '))
        print()
        
        if menu == 1 or menu == 2:
            if menu == 1:
                dadosComputadora = [randrange(1, 6), randrange(1, 6)]
                dadosJugador = [randrange(1, 6), randrange(1, 6)]

                if (dadosComputadora[0] + dadosComputadora[1]) > (dadosJugador[0] + dadosJugador[1]):
                    print(f'Computadora: Dado 1 = {dadosComputadora[0]} - Dado 2 = {dadosComputadora[1]}')
                    print(f'Jugador: Dado 1 = {dadosJugador[0]} - Dado 2 = {dadosJugador[1]}')
                    print('¡¡Gana Computadora!! ')

                    if dadosComputadora[0] != dadosComputadora[1]:
                        computadora += 1
                        print('Suma 1 punto')
                    else:
                        computadora += 2
                        print('Jackpot suma 2 puntos')
                    print()

                elif (dadosComputadora[0] + dadosComputadora[1]) < (dadosJugador[0] + dadosJugador[1]):
                    print(f'Computadora: Dado 1 = {dadosComputadora[0]} - Dado 2 = {dadosComputadora[1]}')
                    print(f'Jugador: Dado 1 = {dadosJugador[0]} - Dado 2 = {dadosJugador[1]}')
                    print('¡¡Gana Jugador!!')
                    if dadosJugador[0] != dadosJugador[1]:
                        jugador += 1
                        print('Suma 1 punto')
                    else:
                        jugador += 2
                        print('Jackpot suma 2 puntos')
                    print()

                elif (dadosComputadora[0] + dadosComputadora[1]) == (dadosJugador[0] + dadosJugador[1]):
                    print(f'Computadora: Dado 1 = {dadosComputadora[0]} - Dado 2 = {dadosComputadora[1]}')
                    print(f'Jugador: Dado 1 = {dadosJugador[0]} - Dado 2 = {dadosJugador[1]}')
                    print('Es un Empate')
                    print()            

            elif menu == 2:
                if jugador > 0 and computadora > 0:    
                    if jugador > computadora:
                        print(f'¡¡Gano Jugador {jugador} a {computadora}!!')
                        print('Gracias por participar')
                        break

                    elif jugador < computadora:
                        print(f'¡¡Gano Computadora {computadora} a {jugador}!!')
                        print('Gracias por participar')
                        break
                    
                else:
                    print('Gracias por participar')
                    break
        
        else:
            print('Ingresa una opcion correcta')    
