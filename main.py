from juego1 import Juego1
from juego2 import Juego2
from juego3 import juego3
from funcion1 import maximo
from poo import CuentaJoven
from graFuncion import graFuncion

class App():
   def __init__(self):
      self.encabezado()
      self.bucle()
      

   
      
   def encabezado(self):   
      print('+-----------------------------------------+')
      print('|              Proyecto Final             |')
      print('+-----------------------------------------+')

   def bucle(self):
      while True:
   
         print('+-----------------------------------------+')
         print('|      Actividad Práctica Integradora     |')
         print('+-----------------------------------------+')
         print('| 1 - Juego Adivina el Numero             |')
         print('| 2 - Juego Piedra Papel y Tijera         |')
         print('| 3 - Juego Tira el Dado                  |')
         print('| 4 - Funcion Maximo y Minimo             |')
         print('| 5 - Poo Simulacion Cuenta Banco         |')
         print('| 6 - Graficar una Funcion                |')         
         print('| 7 - Salir                               |')
         print('+-----------------------------------------+')
         menu = input('Elija un opcion: ')
         if menu == '1':
            print()
            Juego1()

         elif menu == '2':
            print()
            Juego2() 

         elif menu == '3':
            print()
            juego3()

         elif menu == '4':
            print()
            maximo()

         elif menu == '5':
            print()
            CuentaJoven()
            
         elif menu == '6':
            print()
            graFuncion()

         elif menu == '7':
            print('Gracias por participar')
            break 
       
                
        

if __name__ == '__main__':
   App()


