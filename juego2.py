from random import choice

def Juego2():
    print('+-----------------------------------------+')
    print('|           PIEDRA PAPEL TIJERA           |')
    print('+-----------------------------------------+')
    
    
    nombre = input('Hola jugador, ¿como te llamas?: ').capitalize()

    print('Bienvenido ' + nombre + ' al juego de Piedara, Papel y Tijera')

    while True:
        computadora = choice(['Piedra', 'Papel', 'Tijera'])
        print()
        jugador = (input('Elige una opcion - A(piedra) - B(papel) - C(tijera) o escribe Fin : ')).capitalize()
        print()

        if  jugador == 'A' or jugador == 'B' or jugador == 'C' or jugador == 'Fin':
        
            if jugador == 'A':
                if computadora == 'Papel':
                    print(f'Elegiste Piedra y la computadora {computadora}')
                    print('Perdiste')
                elif computadora == 'Tijera':
                    print(f'Elegiste Piedra y la computadora {computadora}')
                    print('Ganaste')
                else:
                    print(f'Elegiste Piedra y la computadora {computadora}')
                    print('Es un Empate')
            elif jugador == 'B':
                if computadora == 'Piedra':
                    print(f'Elegiste Papel y la computadora {computadora}')
                    print('Ganaste')
                elif computadora == 'Tijera':
                    print(f'Elegiste Papel y la computadora {computadora}')
                    print('Perdiste')
                else:
                    print(f'Elegiste Papel y la computadora {computadora}')
                    print('Es un Empate')
            elif jugador == 'C':
                if computadora == 'Piedra':
                    print(f'Elegiste Tijera y la computadora {computadora}')
                    print('Perdista')
                elif computadora == 'Papel':
                    print(f'Elegiste Tijera y la computadora {computadora}')
                    print('Ganaste')
                else:
                    print(f'Elegiste Tijera y la computadora {computadora}')
                    print('Es un Empate')
            elif jugador == 'Fin':
                print('¡¡Gracias por participar!!')
                break

        else :
            print('Ingresa una opcion correcta')    
