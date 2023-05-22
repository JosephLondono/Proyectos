from tkinter import *
from functools import partial


def jugador1(raiz):
    global resultadoJugador1

    raiz.resizable(0,0)
    
    miFrame = Frame(raiz)
    miFrame.pack()

    tituloLabel = Label(miFrame, text="PIEDRA, PAPEL O TIJERA",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=0,column=3, padx=100,pady=20)

    tituloLabel = Label(miFrame, text="JUGADOR 1",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=1,column=3, padx=100,pady=20)

    tituloLabel = Label(miFrame, text="Elije tu opcion",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=2,column=3, padx=100,pady=20)
    
    def hacer_clic_Piedra_Jugador1(raiz):
        global resultadoJugador1
        global imagenResultadoJugador1
        imagenResultadoJugador1 = "piedra.png"
        resultadoJugador1 = "piedra"
        print("Piedra")
        PasarJugador2(raiz)

    def hacer_clic_Papel_Jugador1(raiz):
        global resultadoJugador1
        global imagenResultadoJugador1
        imagenResultadoJugador1 = "papel.png"
        resultadoJugador1 = "papel"
        print("Papel")
        PasarJugador2(raiz)

    def hacer_clic_Tijera_Jugador1(raiz):
        global resultadoJugador1
        global imagenResultadoJugador1
        imagenResultadoJugador1 = "tijera.png"
        resultadoJugador1 = "tijera"
        print("Tijera")
        PasarJugador2(raiz)


    imagenPiedra = PhotoImage(file="piedra.png")
    imagenPiedraMod = imagenPiedra.subsample(30, 30)
    boton_imagenPiedra = Button(miFrame, image=imagenPiedraMod, command=lambda: hacer_clic_Piedra_Jugador1(raiz))
    boton_imagenPiedra.grid(row=4,column=2,padx=50,pady=20)


    imagenPapel = PhotoImage(file="papel.png")
    imagen_Papel_Mod = imagenPapel.subsample(20, 20)
    boton_imagenPapel = Button(miFrame, image=imagen_Papel_Mod, command=lambda: hacer_clic_Papel_Jugador1(raiz))
    boton_imagenPapel.grid(row=4,column=3,pady=20)

    imagenTijera = PhotoImage(file="tijera.png")
    imagen_Tijera_Mod = imagenTijera.subsample(20, 20)
    boton_imagenTijera = Button(miFrame, image=imagen_Tijera_Mod, command=lambda: hacer_clic_Tijera_Jugador1(raiz))
    boton_imagenTijera.grid(row=4,column=4,padx=33,pady=20)

    raiz.mainloop()

def jugador2(raiz):
    global resultadoJugador2
    
    raiz.resizable(0,0)
    
    miFrame = Frame(raiz)
    miFrame.pack()

    tituloLabel = Label(miFrame, text="PIEDRA, PAPEL O TIJERA",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=0,column=3, padx=100,pady=20)

    tituloLabel = Label(miFrame, text="JUGADOR 2",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=1,column=3, padx=100,pady=20)

    tituloLabel = Label(miFrame, text="Elije tu opcion",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=2,column=3, padx=100,pady=20)
    
    def hacer_clic_Piedra_Jugador2(raiz):
        global resultadoJugador2
        global imagenResultadoJugador2
        imagenResultadoJugador2 = "piedra.png"
        resultadoJugador2 = "piedra"
        print("Piedra")
        comprobarGanador(raiz)

    def hacer_clic_Papel_Jugador2(raiz):
        global resultadoJugador2
        global imagenResultadoJugador2
        imagenResultadoJugador2 = "papel.png"
        resultadoJugador2 = "papel"
        print("Papel")
        comprobarGanador(raiz)

    def hacer_clic_Tijera_Jugador2(raiz):
        global resultadoJugador2
        global imagenResultadoJugador2
        imagenResultadoJugador2 = "tijera.png"
        resultadoJugador2 = "tijera"
        print("Tijera")
        comprobarGanador(raiz)

    imagenPiedra = PhotoImage(file="piedra.png")
    imagenPiedraMod = imagenPiedra.subsample(30, 30)
    boton_imagenPiedra = Button(miFrame, image=imagenPiedraMod, command=lambda: hacer_clic_Piedra_Jugador2(raiz))
    boton_imagenPiedra.grid(row=4,column=2,padx=50,pady=20)


    imagenPapel = PhotoImage(file="papel.png")
    imagen_Papel_Mod = imagenPapel.subsample(20, 20)
    boton_imagenPapel = Button(miFrame, image=imagen_Papel_Mod, command=lambda: hacer_clic_Papel_Jugador2(raiz))
    boton_imagenPapel.grid(row=4,column=3,pady=20)

    imagenTijera = PhotoImage(file="tijera.png")
    imagen_Tijera_Mod = imagenTijera.subsample(20, 20)
    boton_imagenTijera = Button(miFrame, image=imagen_Tijera_Mod, command=lambda: hacer_clic_Tijera_Jugador2(raiz))
    boton_imagenTijera.grid(row=4,column=4,padx=33,pady=20)

    raiz.mainloop()

def PasarJugador1(raiz):
    raiz.withdraw()
    raiz.quit()
    jugador1(Toplevel())

def PasarJugador2(raiz):
    raiz.withdraw()
    raiz.quit()
    jugador2(Toplevel())

def salirJuego(ventana):
    ventana.withdraw()
    ventana.quit()
    exit()
    
def comprobarGanador(raiz):
    global resultadoGanador
    if resultadoJugador1 == "piedra" and resultadoJugador2 == "papel":
        resultadoGanador = "GANADOR JUGADOR 2"
    elif resultadoJugador1 == "piedra" and resultadoJugador2 == "tijera":
        resultadoGanador = "GANADOR JUGADOR 1"
    elif resultadoJugador1 == "papel" and resultadoJugador2 == "piedra":
        resultadoGanador = "GANADOR JUGADOR 1"
    elif resultadoJugador1 == "papel" and resultadoJugador2 == "tijera":
        resultadoGanador = "GANADOR JUGADOR 2"
    elif resultadoJugador1 == "tijera" and resultadoJugador2 == "piedra":
        resultadoGanador = "GANADOR JUGADOR 2"
    elif resultadoJugador1 == "tijera" and resultadoJugador2 == "papel":
        resultadoGanador = "GANADOR JUGADOR 1"
    else:
        resultadoGanador = "EMPATE"
    print(resultadoGanador)
    raiz.withdraw()
    raiz.quit()
    mostrarResultado(raiz)

def mostrarResultado(raiz):
    resultadoVentana = Toplevel(raiz)
    resultadoVentana.resizable(0, 0)

    frameResultado = Frame(resultadoVentana)
    frameResultado.pack()

    resultadoLabel = Label(frameResultado, text=resultadoGanador, fg="red", font=("Comic Sans MS", 15))
    resultadoLabel.grid(row=0, column=1, padx=100, pady=20)


    boton_salir = Button(frameResultado, text="Salir", command=lambda: reiniciarJuego(resultadoVentana))
    boton_salir.grid(row=3, column=1, pady=20,padx=20)
    boton_salir.config(width=7, height=1,font=(10),fg="green")


def reiniciarJuego(raiz):
    raiz.withdraw()
    raiz.quit()
    inicioJuego(
        )
    
def inicioJuego():
    raiz = Tk()
    raiz.resizable(0,0)

    ventana = Frame(raiz)
    ventana.pack()

    tituloLabel = Label(ventana, text="PIEDRA, PAPEL O TIJERA",fg="red",font=("Comic Sans MS",15))
    tituloLabel.grid(row=0,column=1, padx=100,pady=20)

    botonJugar = Button(ventana, text="PLAY", command=lambda: PasarJugador1(raiz))
    botonJugar.grid(row=2,column=1,padx=33,pady=20)
    botonJugar.config(bg="#DDE6ED", width=10,height=2)


    botonSalir = Button(ventana, text="EXIT", command=lambda: salirJuego(raiz))
    botonSalir.grid(row=3,column=1,padx=33,pady=20)
    botonSalir.config(bg="#DDE6ED", width=10,height=2)

    raiz.mainloop()

    
inicioJuego()
