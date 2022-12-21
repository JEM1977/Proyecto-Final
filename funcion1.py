'Calculamos el mayor y el menor de una lista de numero crea por el usuario en tiempo real'
def maximo():  
    numeros = []
    i = 1
    while True:
        
        numero = (input(f"Introduce el número # {i} o escribe Fin: ")).capitalize()
        i += 1
        print()
        if numero == 'Fin':
            break
        else:
            
            numeros.append(int(numero))
    
    mayor = numeros[0]
    menor = numeros[0]
    for x in numeros:
        if x > mayor:
            mayor = x
        if x < menor:
            menor = x
    print("El mayor es: ", mayor)
    print("El menor es: ", menor)
   
    print(numeros)
