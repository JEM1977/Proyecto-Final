from random import randrange


def menu_inicio(): 
    
    cant_intentos = 0
    cant_numeros = 0
    nivel = input('Elige el nivel de dificulta A(normal) - B(alto) - C(experto): ').capitalize()
    print()
    
    if nivel == 'A':
        cant_intentos = 6
        cant_numeros = randrange(10, 20)
        print(f'Elegiste la dificulta Normal\nCantidad de numeros: {cant_numeros}\nCantidad de intentos: {cant_intentos}')
        print()
        
    elif nivel == 'B':
        cant_intentos = 6
        cant_numeros = randrange(20, 50)
        print(f'Elegiste la dificulta Alto\nCantidad de numeros: {cant_numeros}\nCantidad de intentos: {cant_intentos}')
        print()
        
    elif nivel == 'C':
        cant_intentos = 6
        cant_numeros = randrange(50, 100)
        print(f'Elegiste la dificulta Experto\nCantidad de numeros: {cant_numeros}\nCantidad de intentos: {cant_intentos}')
        print()
        
    return  cant_numeros, cant_intentos

        

def Juego1(): 
    print('+-----------------------------------------+')
    print('|            ADIVINAR EL NUMERO           |')
    print('+-----------------------------------------+')
    

    nombre = input('¡¡Buenos dias Usuario!!\n¿Como te llamas?: ').capitalize()
    print()

    print(f'¡¡Bienvenido {nombre} al juego de Adivinar el Numero!!')
    print('El juego consiste en adivinar mi numero en un determinado numero de intentos')
    print()

    cant_numeros, cant_intentos = menu_inicio()
    intentos = 0
    numero_cpu = randrange(cant_numeros)
 
    while intentos <= cant_intentos : 

        if intentos == cant_intentos:
            print(f'Lo siento as perdido, el numero era {numero_cpu}')
            jugar = input('¿Quieres que volvamos a jugar? SI o No: ').capitalize()
            print()
            if jugar == 'Si':
                cant_numeros, cant_intentos = menu_inicio()                            
                intentos = 0
                numero_cpu = randrange(cant_numeros)
                
            elif jugar == 'No':
                print('¡¡Gracias por haber participado!!')
                break

        
        if intentos == (cant_intentos - 1):
            print('Cuidado te queda 1 intento, piensalo bien......')

        intentos += 1
        numero_usario = int(input('Ingresa un numero entero: '))
        print()
        
        if numero_usario > numero_cpu:        
            print(f'Lo siento {nombre} estas un poco alto, vuelve a intentarlo')
            print()
            
        elif numero_usario < numero_cpu:        
            print(f'Lo siento {nombre} estas un poco bajo, vuelve a intentarlo')   
            print()
            
        elif numero_usario == numero_cpu:        
            print(f'Felicitaciones {nombre} as acertado el numero')
            print()
            jugar = input('¿Quieres que volvamos a jugar? SI o No: ').capitalize()
            print()
            if jugar == 'Si':
                cant_numeros, cant_intentos = menu_inicio()                            
                intentos = 0
                numero_cpu = randrange(cant_numeros)
                
            elif jugar == 'No':
                print('¡¡Gracias por haber participado!!')
                break

