import tkinter as tk
from tkinter import messagebox
import random
import time

class Cuestionario_multimateria:

    # Funciones de Inicialización
    def __init__(self, master):
        self.master = master
        master.title("Cuestionario")  
        master.geometry("400x600")  
        master.configure(bg="#f0f0f0")  # Color de fondo
        master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Manejo del cierre de ventana

        self.puntaje = 0  
        self.contador_preguntas = 0  
        self.preguntas = []  # Lista para almacenar preguntas
        self.pregunta_actual = None  # Pregunta actual
        self.subject = ""  # Tema seleccionado
        self.hora_de_inicio = 0  
        self.tiempo_total = 0  
        self.cuestionario_en_progreso = False 
        self.id_temporizador = None 
        self.setup_ui()  # Configuración de la interfaz de usuario

    def setup_ui(self):
        self.clear_window()  # Limpiar la ventana antes de configurar


        # Etiqueta para seleccionar un tema
        self.etiqueta_seleccion = tk.Label(self.master, text="Selecciona un tema:", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.etiqueta_seleccion.pack(pady=20)

        self.sujeto_var = tk.StringVar()  # Variable para almacenar el tema seleccionado
        self.sujeto_var.set(None)  # Establece el valor inicial
        subjects = ["Matemáticas", "Lenguaje", "Ciencias Sociales"]  
        for subject in subjects:
            tk.Radiobutton(self.master, text=subject, variable=self.sujeto_var, value=subject,
            font=("Arial", 14), bg="#f0f0f0").pack(pady=5)  # Botones de opción para los temas


        # Botón para comenzar el cuestionario
        self.start_button = tk.Button(self.master, text="Comenzar", command=self.start_quiz,
        font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", width=12)
        self.start_button.pack(pady=15)


        # Elementos de la interfaz para el cuestionario
        self.etiqueta_pregunta = tk.Label(self.master, text="", font=("Arial", 16, "italic"), bg="#f0f0f0", wraplength=380)
        self.etiqueta_temporizador = tk.Label(self.master, text="", font=("Arial", 14), bg="#f0f0f0")
        self.entrada_de_respuesta = tk.Entry(self.master, font=("Arial", 14), justify="center")


        # Botón para enviar respuesta
        self.boton_enviar = tk.Button(self.master, text="Enviar respuesta", command=self.comprobar_respuests,
        font=("Arial", 12), bg="#FFEB3B", relief="raised", width=12)


        # Etiquetas para mostrar resultados y puntaje
        self.resultado_actual = tk.Label(self.master, text="", font=("Arial", 14), bg="#f0f0f0", wraplength=380)
        self.etiqueta_puntuación = tk.Label(self.master, text="Puntaje: 0", font=("Arial", 14), bg="#f0f0f0")


        # Botones para finalizar y regresar a la selección de temas
        self.boton_terminar = tk.Button(self.master, text="Finalizar", command=self.finish_quiz,
        font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", width=12)

        self.boton_regresar = tk.Button(self.master, text="Regresar a temas", command=self.reset_quiz,
        font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", width=12)


    def clear_window(self):
        # Limpiar todos los widgets de la ventana
        for widget in self.master.winfo_children():
            widget.pack_forget()


    def start_quiz(self):
        # Comenzar el cuestionario
        self.subject = self.sujeto_var.get()  # Obtener tema seleccionado
        if self.subject:
            self.clear_window()  
            self.cuestionario_en_progreso = True  # Inicia el cuestionario
            self.puntaje = 0  # Reiniciar puntaje
            self.contador_preguntas = 0  
            self.tiempo_total = 0  
            self.preguntas.clear()  # Limpiar lista de preguntas
            self.generate_preguntas()  # Generar preguntas según el tema
            

            # Mostrar elementos de la interfaz
            self.etiqueta_pregunta.pack(pady=20)
            self.etiqueta_temporizador.pack(pady=5)
            self.entrada_de_respuesta.pack(pady=10)
            self.boton_enviar.pack(pady=10)
            self.resultado_actual.pack(pady=10)
            self.etiqueta_puntuación.pack(pady=10)
            self.boton_terminar.pack(pady=15)
            self.boton_regresar.pack(pady=15)
            
            self.next_question() 
        else:
            messagebox.showinfo("Error", "Por favor, selecciona un tema.") 

    def generate_preguntas(self):
        # Generar preguntas según el tema seleccionado
        if self.subject == "Matemáticas":
            self.generate_math_preguntas()
        elif self.subject == "Lenguaje":
            self.generate_language_preguntas()
        elif self.subject == "Ciencias Sociales":
            self.generate_social_science_preguntas()

    def generate_math_preguntas(self):
        # Generar preguntas de matemáticas
        operations = ['+', '-', '*', '/']  
        for _ in range(16):
            op = random.choice(operations)  
            if op == '/':
                num2 = random.randint(1, 10)  # Asegurarse de que num1 sea divisible por num2
                num1 = num2 * random.randint(1, 10)
                result = num1 // num2  # División entera
            else:
                num1 = random.randint(1, 10)  # Números aleatorios
                num2 = random.randint(1, 10)
                result = self.calculate(num1, num2, op)  
            self.preguntas.append((f"{num1} {op} {num2} = ?", str(result)))  # Agregar pregunta a la lista

    def calculate(self, num1, num2, op):
        # Calcular el resultado de la operación
        if op == '+': return num1 + num2
        elif op == '-': return num1 - num2
        elif op == '*': return num1 * num2

    def generate_language_preguntas(self):
        # Generar preguntas de lenguaje
        preguntas = [
            ("¿Qué es un sustantivo?", "palabra que nombra personas, animales, cosas o lugares"),
            ("Escribe tres ejemplos de palabras que sean adjetivos.", "bonito, alto, grande"),
            ("¿Qué signos utilizamos para hacer una pregunta?", "signos de interrogación ¿?"),
            ("¿Qué es un verbo?", "palabra que indica una acción"),
            ("¿Cuál es el plural de 'flor'?", "flores"),
            ("Escribe el antónimo de 'grande'.", "pequeño"),
            ("¿Qué es una oración?", "conjunto de palabras que expresan una idea completa"),
            ("¿Qué palabra usamos para describir cómo sucede una acción?", "adverbio"),
            ("¿Cuál es el diminutivo de 'perro'?", "perrito"),
            ("¿Qué es un adjetivo?", "palabra que describe al sustantivo"),
            ("Escribe tres ejemplos de pronombres.", "yo, tú, él"),
            ("¿Qué signos utilizamos para hacer una exclamación?", "signos de exclamación ¡!"),
            ("¿Qué es un sinónimo?", "palabra que tiene un significado similar a otra"),
            ("¿Qué es un antónimo?", "palabra que tiene un significado opuesto a otra"),
            ("¿Qué es un sujeto en una oración?", "la persona, animal o cosa de la que se habla en la oración"),
            ("Escribe un ejemplo de una oración interrogativa.", "¿Cómo te llamas?")
        ]
        self.preguntas = random.sample(preguntas, 16) 

    def generate_social_science_preguntas(self):
        # Generar preguntas de ciencias sociales
        preguntas = [
            ("¿Qué es una comunidad?", "grupo de personas que viven en un mismo lugar y comparten cosas en común"),
            ("Nombra tres servicios que ofrece tu comunidad.", "escuela, hospital, parque"),
            ("¿Qué es un mapa?", "una representación de un lugar"),
            ("¿Cuáles son los nombres de los puntos cardinales?", "norte, sur, este, oeste"),
            ("¿Qué es una familia?", "grupo de personas unidas por lazos de sangre o convivencia"),
            ("¿Qué es una tradición?", "una costumbre que se pasa de generación en generación"),
            ("¿Qué es un país?", "un territorio con fronteras y un gobierno propio"),
            ("Nombra dos medios de transporte en tu comunidad.", "autobús, bicicleta"),
            ("¿Quién es el alcalde?", "la persona que dirige la ciudad o comunidad"),
            ("Nombra dos tipos de paisajes naturales.", "montañas, ríos"),
            ("¿Qué es una frontera?", "una línea que separa territorios o países"),
            ("¿Qué es una ciudad?", "un lugar donde viven muchas personas con servicios y edificios"),
            ("¿Qué colores tiene la bandera de tu país?", "depende del país, por ejemplo, azul y blanco para Guatemala"),
            ("Nombra dos continentes.", "América, Europa"),
            ("¿Qué es un lago?", "una gran extensión de agua rodeada de tierra"),
            ("¿Qué es una capital?", "la ciudad más importante de un país o región donde se encuentra el gobierno")
        ]
        self.preguntas = random.sample(preguntas, 16)  


    def next_question(self):
        # Mostrar la siguiente pregunta
        if self.contador_preguntas < len(self.preguntas):
            self.pregunta_actual = self.preguntas[self.contador_preguntas]  # Obtener la pregunta actual
            self.etiqueta_pregunta.config(text=self.pregunta_actual[0])  # Mostrar la pregunta
            self.entrada_de_respuesta.delete(0, tk.END)  # Limpiar entrada de respuesta
            self.hora_de_inicio = time.time()  # Reiniciar el temporizador
            self.update_timer()  # Actualizar el temporizador
        else:
            self.show_final_results()  # Mostrar resultados finales


    def update_timer(self):
        # Actualizar el temporizador
        if self.cuestionario_en_progreso:
            tiempo_transcurrido = int(time.time() - self.hora_de_inicio)  # Calcular tiempo transcurrido
            tiempo_restante = max(0, 20 - tiempo_transcurrido)  # Calcular tiempo restante
            self.etiqueta_temporizador.config(text=f"Tiempo restante: {tiempo_restante} segundos")  # Mostrar tiempo restante
            if tiempo_restante > 0:
                self.id_temporizador = self.master.after(1000, self.update_timer)  # Actualizar cada segundo
            else:
                self.comprobar_respuests()  # Comprobar respuesta si se acaba el tiempo


    def comprobar_respuests(self):
        # Comprobar la respuesta del usuario
        if self.cuestionario_en_progreso:
            if self.id_temporizador:
                self.master.after_cancel(self.id_temporizador)  
            tiempo_transcurrido = int(time.time() - self.hora_de_inicio)  
            self.tiempo_total += tiempo_transcurrido  # Sumar al tiempo total

            comprobar_respuests = self.entrada_de_respuesta.get().strip().lower()  # Obtener respuesta del usuario
            respuesta_correcta = self.pregunta_actual[1].lower()  # Obtener respuesta correcta


            # Comparar respuestas y actualizar puntaje
            if comprobar_respuests == respuesta_correcta:
                self.resultado_actual.config(text="¡Correcto!", fg="green")  # Mensaje de respuesta correcta
                self.puntaje += 1  # Incrementar puntaje
            else:
                self.resultado_actual.config(text=f"Incorrecto. La respuesta correcta era: {self.pregunta_actual[1]}", fg="red")  

            self.contador_preguntas += 1  # Incrementar contador de preguntas
            self.update_etiqueta_puntuación()  
            self.next_question()  


    def update_etiqueta_puntuación(self):
        # Actualizar etiqueta de puntaje
        self.etiqueta_puntuación.config(text=f"Puntaje: {self.puntaje}")


    def show_final_results(self):
        # Mostrar resultados finales al terminar el cuestionario
        self.cuestionario_en_progreso = False  # Cambiar estado del cuestionario
        minutes, seconds = divmod(self.tiempo_total, 60)  # Calcular minutos y segundos
        messagebox.showinfo("Resultados Finales", 
                            f"¡Felicidades!\nTu puntaje final es: {self.puntaje}\n"
                            f"Tiempo total: {minutes} minutos y {seconds} segundos")  # Mostrar resultados
        if self.puntaje < 7:
            self.reset_quiz()  # Reiniciar cuestionario si el puntaje es bajo
        else:
            self.boton_terminar.config(state=tk.NORMAL)  # Habilita el botón de finalizar


    def finish_quiz(self):
        # Finalizar el cuestionario
        if self.puntaje >= 7:
            minutes, seconds = divmod(self.tiempo_total, 60)  # Calcular minutos y segundos
            messagebox.showinfo("Resumen Final", 
                                f"Tu puntaje final es: {self.puntaje}\n"
                                f"Tiempo total: {minutes} minutos y {seconds} segundos")  # Mostrar resumen final
            self.master.quit()  # Cerrar la aplicación
        else:
            messagebox.showinfo("No se puede finalizar", 
                                "Debes obtener al menos 7 puntos para finalizar el juego.") 
            

    def reset_quiz(self):
        # Reiniciar el cuestionario
        self.cuestionario_en_progreso = False  # Cambiar estado del cuestionario
        self.puntaje = 0 
        self.contador_preguntas = 0 
        self.preguntas.clear()  
        self.sujeto_var.set("")  
        self.tiempo_total = 0 
        if self.id_temporizador:
            self.master.after_cancel(self.id_temporizador)  # Cancelar temporizador si está activo
        self.setup_ui()  # Configurar interfaz de usuario


    def on_closing(self):
        # Manejar el cierre de la ventana
        if self.cuestionario_en_progreso:
            messagebox.showinfo("No se puede salir", 
                                "Debes obtener al menos 7 puntos y presionar 'Finalizar' para salir del juego.")
        else:
            self.master.quit()  # Cerrar la aplicación


if __name__ == "__main__":
    root = tk.Tk()  # Crea la instancia de la ventana principal
    quiz_app = Cuestionario_multimateria(root)  # Crea el objeto del cuestionario
    root.mainloop()  # Inicia mi bucle principal de la interfaz
