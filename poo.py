
class Persona:
    def __init__(self):
        self.titulo()
        self.nombre = input('Ingrese su nombre completo: ').title()
        self.edad = int(input('Ingrese su edad: '))
        print()
        
    def mostrar(self):
        print(f'Su nombre es: {self.nombre}')
        print(f'Su edad es: {self.edad}')
        print()
        
    def mayor_edad(self):
        if self.edad >= 18:
            print('Eres mayor de edad')
        else:
            print('Eres menor de edad')
        print()

    def titulo(self):
        print('+-----------------------------------------+')
        print('|           CUENTA JOVEN                  |')
        print('+-----------------------------------------+')
        print('Condicion de la cuenta:\nSer mayor de 18 y menor de 25')
        print()
        
class Cuenta(Persona):
    def __init__(self):
        super(). __init__()
        self.valido = False
        self.saldoCuenta = 0
        
    def mostrar_cuenta(self):
        print(f'Titular de la cuenta: {self.nombre} ') 
        print(f'Saldo de la cuenta: {self.saldoCuenta}')   
        print()
                       
    def menu_cuenta(self):
        while True:
            print('+--------------------------------+')
            print('|          Menu Cuenta           |')
            print('+--------------------------------+')
            print('| (1)-Ingresar dinero            |') 
            print('| (2)-Retirar dinero             |')
            print('| (3)-Salir                      |')
            print('+--------------------------------+')
            menu = (input('Ingrese una opcion: '))

            if menu == '1':
                self.ingresar = int(input('Indique la cantidad que desea ingresar: '))
                self.saldoCuenta += self.ingresar 
                print(f'Saldo de la cuenta: {self.saldoCuenta}')  
                print()

            elif menu == '2':
                while True:    
                    if self.valido == True:
                        if self.saldoCuenta > 0: 
                            self.retirar = int(input('Indique la cantidad que desea retirar: '))
                            if self.retirar <= self.saldoCuenta:
                                self.saldoCuenta -= self.retirar
                                print(f'Saldo de la cuenta: {self.saldoCuenta}')  
                                break
                            else:
                                print('No cuenta con suficiente fondos.') 
                                print(f'Saldo de la cuenta: {self.saldoCuenta}')  
                                break 
                            
                        else:
                            print('No cuenta con suficiente fondos.')  
                            break 
       
                    else:
                        print('La cuenta no es valida no podra realizar retiros.')
                        break
                    
            elif menu == '3':
                break
 
class CuentaJoven(Cuenta):
    def __init__(self):
        super(). __init__()
        self.mostrar()
        self.mostrar_cuenta()
        self.titularValido()        
        self.menu_cuenta()
    
    def titularValido(self):
        if self.edad >= 18 and self.edad < 25:
            self.valido = True

