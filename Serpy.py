import turtle #Biblioteca para gráficas básicas 
import time 
import random 
import tkinter as tk # Para crear ventanas de interfaz adicionales
import subprocess  # Para ejecutar otros archivos Python

# Nuestra forma (con alias)
from tkinter import font as tkfont #Uso: tkfont.Font


# Configuración inicial
ancho = 600
alto = 600
Tamaño_celda = 20


#Variables de control
posponer = 0.1  # Velocidad inicial
puntaje = 0 # Puntaje actual
puntaje_alto = 0 # Puntaje alcanzado
ultimo_incremento = 0 # Último punto donde se aumentó la velocidad
juego_pausado = False
juego_terminado = False


# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.setup(width=ancho, height=alto)
wn.bgpic("download.png")  
wn.tracer(0) # Desactiva la animación automática para mejor rendimiento


# Creación de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("dark green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"


# Agregar la forma de la manzana
wn.addshape("Manzana2.gif")


# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("Manzana2.gif")
comida.color("red")
comida.penup()
comida.goto(0, 100)


# Cuerpo Serpiente
segmentos = []


# Texto
Texto = turtle.Turtle()
Texto.speed(0)
Texto.color("white")
Texto.penup()
Texto.hideturtle()
Texto.goto(0, alto // 2 - 40)
Texto.write("Punteo: 0      Punteo más alto: 0", align="center", font=("Courier", 20, "normal"))


# Mensaje de velocidad
MensajeVelocidad = turtle.Turtle()
MensajeVelocidad.speed(0)
MensajeVelocidad.color("yellow")
MensajeVelocidad.penup()
MensajeVelocidad.hideturtle()
MensajeVelocidad.goto(0, 0)


# Funciones de movimiento
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"


#Funciones de movimiento principal
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + Tamaño_celda)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - Tamaño_celda)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - Tamaño_celda)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + Tamaño_celda)


#Todo termina
def Fin_del_juego():
    global puntaje, ultimo_incremento, juego_pausado
    juego_pausado = True
    time.sleep(1)
    Texto.goto(0, 0)
    Texto.write("Abriendo cuestionario...", align="center", font=("Arial", 20, "normal"))
    wn.update()
    time.sleep(2)
    abrir_cuestionario()


#Abre mi cuestionario
def abrir_cuestionario():
    subprocess.Popen(["python", "Preguntas.py"])



def mostrar_ventana_instrucciones():
    ventana = tk.Tk()
    ventana.title("Instrucciones del Juego de Snake")
    ventana.geometry("500x300")
    ventana.configure(bg='#2C3E50')  # Fondo oscuro

    # Estilo de fuente
    titulo_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
    texto_font = tkfont.Font(family="Helvetica", size=12)

    # Título
    tk.Label(ventana, text="¡Bienvenido al Juego de Snake!", 
             font=titulo_font, bg='#2C3E50', fg='#ECF0F1').pack(pady=10)
    
     # Instrucciones
    instrucciones = [
        "Usa las flechas del teclado para mover a la serpiente",
        "Presiona 't' para pausar o reanudar el juego",
        "Presiona 'r' para reiniciar el juego",
        "Come las manzanas para crecer y ganar puntos",
        "¡Cuidado! No choques con los bordes ni contigo mismo"
    ]

    for instruccion in instrucciones:
        tk.Label(ventana, text=f"• {instruccion}", 
                 font=texto_font, bg='#2C3E50', fg='#ECF0F1', 
                 anchor='w', justify='left').pack(pady=5, padx=20)

    # Cerrar ventana después de 8 segundos
    ventana.after(8000, ventana.destroy)


#Reinicia mi juego...
def reiniciar_juego():
    global puntaje, ultimo_incremento, juego_pausado, posponer
    puntaje = 0
    ultimo_incremento = 0
    posponer = 0.1
    juego_pausado = False
    cabeza.goto(0, 0)
    cabeza.direction = "stop"

    for segmento in segmentos:
        segmento.goto(1000, 1000)  # Mueve los segmentos fuera de la pantalla
    segmentos.clear()
    actualizar_puntaje()
    comida.goto(0, 100)

    #Abre la ventana de instrucciones
    mostrar_ventana_instrucciones()


#Para que cuando este llegue al nuevo puntaje lo guarde 
def actualizar_puntaje():
    Texto.clear()
    Texto.goto(0, 260)
    Texto.write("Punteo: {}      Punteo más alto: {}".format(puntaje, puntaje_alto),
                align="center", font=("Courier", 20, "normal"))


#Muestra el mensaje de velocidad que se incrementa 
def incrementar_velocidad():
    global posponer, ultimo_incremento
    posponer *= 0.9
    ultimo_incremento = puntaje
    MensajeVelocidad.clear()
    MensajeVelocidad.write("¡Velocidad aumentada!", align="center", font=("Arial", 20, "normal"))
    wn.update()
    wn.ontimer(MensajeVelocidad.clear, 1000)


#Para poder pausar el juego 
def pausa():
    global juego_pausado
    juego_pausado = not juego_pausado
    if juego_pausado:
        Texto.goto(0, 0)
        Texto.write("JUEGO PAUSADO", align="center", font=("Arial", 24, "normal"))
    else:
        Texto.clear()
        actualizar_puntaje()
        wn.ontimer(Bucle_principal_juego, int(posponer * 1000))


#Mi ventana para brindar las instrucciones
def mostrar_instrucciones():
    mostrar_ventana_instrucciones()


# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
wn.onkeypress(pausa, "t")  # Añadi la tecla para pausar/reanudar
wn.onkeypress(reiniciar_juego, "r")  # Añadi la tecla para reiniciar


def Bucle_principal_juego():
    global puntaje, puntaje_alto, juego_pausado

    if not juego_pausado:
        wn.update()
        
        # Condiciones Bordes
        if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            Fin_del_juego()
        

        # Colisiones con la comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 240)
            comida.goto(x, y)


            #Agrega más segmentos a la serpiente cada que se come la manzana
            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("Green")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)
            
            puntaje += 1
            if puntaje > puntaje_alto:
                puntaje_alto = puntaje
            actualizar_puntaje()

            # Incrementar velocidad cada 5 puntos
            if puntaje % 5 == 0 and puntaje != ultimo_incremento:
                incrementar_velocidad()

        
        # Mover el cuerpo de la serpiente
        totalSeg = len(segmentos)
        for index in range(totalSeg - 1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x, y)
        
        if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos[0].goto(x, y)
        mov()
        
        # Colisiones con el cuerpo
        for segmento in segmentos:
            if segmento.distance(cabeza) < 20:
                Fin_del_juego()
        wn.ontimer(Bucle_principal_juego, int(posponer * 1000))
    else:
        wn.ontimer(Bucle_principal_juego, 100)  # Comprueba el estado de pausa cada 100ms


# Mostrar instrucciones al inicio del juego
mostrar_instrucciones()

Bucle_principal_juego()
wn.mainloop()