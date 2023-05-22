from piedra import *
from tijera import *
from papel import *
from incog import *
from esquis import *

def vacio():
    print("|","                                                   |")

def linea():
    print("|","="*50,"|")
    
def titulos():
    print("|","="*50,"|")
    print("|","             ","PIEDRA, PAPEL O TIJERA","              |")
    print("|","="*50,"|")

def final():
    print("|","="*50,"|")
    print("|","                 ","JUEGO TERMINADO","                 |")
    print("|","="*50,"|")
    
def player1(jugador1):
    global Resultjugador1
    if jugador1 == None:
        return esqui()
    elif jugador1 == 1:
        Resultjugador1 = 1
        return piedra()
    elif jugador1 == 2:
        Resultjugador1 = 2
        return papel()
    elif jugador1 == 3:
        Resultjugador1 = 3
        return tijera()

        
def player2(jugador2):
    global Resultjugador2
    if jugador2 == None:
        return esqui()
    elif jugador2 == 1:
        Resultjugador2 = 1
        return piedra()
    elif jugador2 == 2:
        Resultjugador2 = 2
        return papel()
    elif jugador2 == 3:
        Resultjugador2 = 3
        return tijera()

def comprobarGanador(jugador1,jugador2):
    if jugador1 == 1 and jugador2 == 2:
        print("|", "               GANADOR JUGADOR 2","                  |")
    elif jugador1 == 1 and jugador2 == 3:
        print("|", "               GANADOR JUGADOR 1","                  |")
    elif jugador1 == 1 and jugador2 == 1:
        print("|", "                    EMPATE","                        |")
    elif jugador1 == 2 and jugador2 == 1:
        print("|", "               GANADOR JUGADOR 1","                  |")
    elif jugador1 == 2 and jugador2 == 3:
        print("|", "               GANADOR JUGADOR 2","                  |")
    elif jugador1 == 2 and jugador2 == 2:
        print("|", "                    EMPATE","                        |")
    elif jugador1 == 3 and jugador2 == 1:
        print("|", "               GANADOR JUGADOR 2","                  |")
    elif jugador1 == 3 and jugador2 == 2:
        print("|", "               GANADOR JUGADOR 1","                  |")
    elif jugador1 == 3 and jugador2 == 3:
        print("|", "                    EMPATE","                        |")

        
def iniciarJuego():
    while True:
        jugador1 = None
        jugador2 = None
        titulos()
        print("|","                ","QUE QUIERES HACER","                |")
        vacio(
            )
        print("|", "               ESCRIBE 1 PARA JUGAR","               |")
        print("|", "               ESCRIBE 10 PARA SALIR","              |")
        print("|","="*50,"|")
        print("|","                     ","OPCION","                      |")
        opcion = int(input("                          "))
        print("")
        if opcion == 1:
            titulos()
            print("|","                    ","JUGADOR 1","                   ","|")
            vacio()
            player1(jugador1)
            linea()
            print("|","                    ","JUGADOR 2","                   ","|")
            vacio()
            player2(jugador2)
            linea()
            print("|", "             JUGADOR 1 ELIJE TU OPCION","            |")
            print("|", "               ESCRIBE 1 PARA PIEDRA","              |")
            print("|", "               ESCRIBE 2 PARA PAPEL","               |")
            print("|", "               ESCRIBE 3 PARA TIJERA","              |")
            while True:
                jugador1 = int(input())
                if jugador1 != 1 and jugador1 != 2 and jugador1 != 3:
                    print("|", "                  OPCION ERRONEA","                  |")
                else:
                    break
            linea()
            print("|","                    ","JUGADOR 1","                   ","|")
            vacio()
            incog()
            linea()
            print("|", "             JUGADOR 2 ELIJE TU OPCION","            |")
            print("|", "               ESCRIBE 1 PARA PIEDRA","              |")
            print("|", "               ESCRIBE 2 PARA PAPEL","               |")
            print("|", "               ESCRIBE 3 PARA TIJERA","              |")
            while True:
                jugador2 = int(input())
                if jugador2 != 1 and jugador2 != 2 and jugador2 != 3:
                    print("|", "                  OPCION ERRONEA","                  |")
                else:
                    break
            vacio()
            incog()
            linea()
            print("|","                    ","JUGADOR 1","                   ","|")
            vacio()
            player1(jugador1)
            linea()
            print("|","                    ","JUGADOR 2","                   ","|")
            player2(jugador2)
            linea()
            comprobarGanador(Resultjugador1,Resultjugador2)
            final()
        elif opcion == 10:
            final()
            break
        
        else:
            print("|", "                  OPCION ERRONEA","                  |")
        
    

