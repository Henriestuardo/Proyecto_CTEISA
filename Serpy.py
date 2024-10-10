import os
import turtle
import time
import random
import tkinter as tk

posponer = 0.1

# Marcador
score = 0
high_score = 0

# Configuración de la ventana del juego
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.setup(width=600, height=600)
wn.bgpic("download.png")  # Asegúrate de tener esta imagen en la misma carpeta
wn.tracer(0)

# Cabeza Serpiente 
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
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
Texto.goto(0, 260)
Texto.write("Punteo: 0      Punteo más alto: 0", align="center", font=("Courier", 20, "normal"))

# Funciones 
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

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def game_over():
    global score
    time.sleep(1)
    Texto.goto(0, 0)
    Texto.write("Abriendo cuestionario...", align="center", font=("Arial", 20, "normal"))
    wn.update()
    time.sleep(2)
    abrir_cuestionario()

def abrir_cuestionario():
    # Cierra el juego de la serpiente y abre el cuestionario
    wn.bye()
    os.system('python Preguntas.py')  # Asegúrate de que Preguntas.py esté en el mismo directorio

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Bucle Verdadero
while True:
    wn.update()

    # Condiciones Bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        game_over()

    # Colisiones con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 240)  # Limite el rango superior para evitar que la comida aparezca en el marcador
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # Aumentar Marcador
        score += 1

        if score > high_score:
            high_score = score
        Texto.clear()
        Texto.write("Punteo: {}      Punteo más alto: {}".format(score, high_score), 
                    align="center", font=("Courier", 20, "normal"))

    # Cuerpo Serpiente
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
            game_over()

    time.sleep(posponer)
