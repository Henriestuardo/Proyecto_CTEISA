import tkinter as tk
import random

class MultiSubjectQuiz:
    def __init__(self, master):
        self.master = master
        master.title("Cuestionario")
        master.geometry("400x600")
        master.configure(bg="#f0f0f0")

        self.score = 0
        self.question_count = 0
        self.questions = []
        self.current_question = None
        self.subject = ""

        self.subject_label = tk.Label(master, text="Selecciona un tema:", font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.subject_label.pack(pady=20)

        self.subject_var = tk.StringVar()
        subjects = ["Matemáticas", "Lenguaje", "Ciencias Sociales"]
        for subject in subjects:
            tk.Radiobutton(master, text=subject, variable=self.subject_var, value=subject,
            font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

        self.start_button = tk.Button(master, text="Comenzar", command=self.start_quiz,
        font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised", width=12)
        self.start_button.pack(pady=15)

        self.question_label = tk.Label(master, text="", font=("Arial", 16, "italic"), bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 14), justify="center")
        self.answer_entry.pack(pady=10)
        self.answer_entry.pack_forget()

        self.send_button = tk.Button(master, text="Enviar respuesta", command=self.check_answer,
        font=("Arial", 12), bg="#FFEB3B", relief="raised", width=12)
        self.send_button.pack(pady=10)
        self.send_button.pack_forget()

        self.result_label = tk.Label(master, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Puntaje: 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.finish_button = tk.Button(master, text="Finalizar", command=self.finish_quiz,
        font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", width=12)
        self.finish_button.pack(pady=15)
        self.finish_button.pack_forget()

        self.back_button = tk.Button(master, text="Regresar a temas", command=self.reset_quiz,
        font=("Arial", 12), bg="#FF9800", fg="white", relief="raised", width=12)
        self.back_button.pack(pady=15)
        self.back_button.pack_forget()

        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if self.score >= 7:
            self.master.quit()
        else:
            self.result_label.config(text="Debes obtener al menos 7 puntos para salir.")

    def start_quiz(self):
        self.subject = self.subject_var.get()
        if self.subject:
            self.generate_questions()
            self.next_question()

            self.start_button.pack_forget()
            self.subject_label.pack_forget()
            for widget in self.master.winfo_children():
                if isinstance(widget, tk.Radiobutton):
                    widget.pack_forget()

            self.answer_entry.pack()
            self.send_button.pack()
            self.back_button.pack()
            self.finish_button.pack()

        else:
            self.result_label.config(text="Por favor, selecciona un tema.")

    def generate_questions(self):
        if self.subject == "Matemáticas":
            self.generate_math_questions()
        elif self.subject == "Lenguaje":
            self.generate_language_questions()
        elif self.subject == "Ciencias Sociales":
            self.generate_social_science_questions()



    def generate_math_questions(self):
        operations = ['+', '-', '*', '/']
        for _ in range(16):  # 16 preguntas en total
            op = random.choice(operations)
            num1 = random.randint(1, 10)  # Limitar a 1-10 para simplificar
            num2 = random.randint(1, 16)

            if op == '-':
                num1 = max(num1, num2)
            elif op == '/':
                # Asegura que la división sea simple
                num1 = num1 * num2  # Asegura que la división sea exacta
                num2 = random.randint(1, 10)  # Mantener divisor pequeño

            if op == '/':
                result = num1 // num2  # División entera
            else:
                result = self.calculate(num1, num2, op)

            self.questions.append((f"{num1} {op} {num2} = ?", str(result)))

    def calculate(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        


    def generate_language_questions(self):
        questions = [
            ("¿Cuál es el plural de 'lápiz'?", "lápices"),
            ("¿Cuál es el antónimo de 'alegre'?", "triste"),
            ("¿Qué tipo de palabra es 'rápidamente'?", "adverbio"),
            ("¿Cuál es el pretérito perfecto simple de 'andar'?", "anduve"),
            ("¿Cuál es el complemento directo en 'Juan lee un libro'?", "un libro"),
            ("¿Qué figura literaria es 'El viento susurra'?", "personificación"),
            ("¿Cuál es el superlativo de 'bueno'?", "óptimo"),
            ("¿Qué tipo de oración es 'Ojalá llueva mañana'?", "desiderativa"),
            ("¿Cuál es el gerundio de 'decir'?", "diciendo"),
            ("¿Qué es un palíndromo?", "palabra que se lee igual al revés"),
            ("¿Cuál es el participio de 'romper'?", "roto"),
            ("¿Qué es una onomatopeya?", "palabra que imita un sonido"),
            ("¿Cuál es el aumentativo de 'perro'?", "perrazo"),
            ("¿Qué tipo de palabra es 'aunque'?", "conjunción"),
            ("¿Cuál es el modo verbal en 'Quizás venga mañana'?", "subjuntivo"),
            ("¿Qué es un sinónimo de 'efímero'?", "fugaz")
        ]
        self.questions = random.sample(questions, min(len(questions), 16))

    def generate_social_science_questions(self):
        questions = [
            ("¿En qué año se descubrió América?", "1492"),
            ("¿Cuál es la capital de Francia?", "París"),
            ("¿Quién pintó 'La noche estrellada'?", "Van Gogh"),
            ("¿En qué continente está Egipto?", "África"),
            ("¿Cuál es el río más largo del mundo?", "Amazonas"),
            ("¿Quién fue el primer presidente de Estados Unidos?", "George Washington"),
            ("¿En qué año comenzó la Primera Guerra Mundial?", "1914"),
            ("¿Cuál es la montaña más alta del mundo?", "Everest"),
            ("¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez"),
            ("¿Cuál es el océano más grande?", "Pacífico"),
            ("¿En qué año cayó el Muro de Berlín?", "1989"),
            ("¿Cuál es el país más poblado del mundo?", "China"),
            ("¿Quién fue el líder de los derechos civiles en EE.UU.?", "Martin Luther King Jr."),
            ("¿Cuál es la moneda de Japón?", "Yen"),
            ("¿En qué año terminó la Segunda Guerra Mundial?", "1945"),
            ("¿Quién pintó la Mona Lisa?", "Leonardo da Vinci")
        ]
        self.questions = random.sample(questions, min(len(questions), 16))

    def next_question(self):
        if self.question_count < len(self.questions):
            self.current_question = self.questions[self.question_count]
            self.question_label.config(text=self.current_question[0])
            self.answer_entry.delete(0, tk.END)
        else:
            self.finish_quiz()

    def check_answer(self):
        check_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_question[1].lower()

        if check_answer == correct_answer:
            self.result_label.config(text="¡Correcto!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrecto. La respuesta correcta era: {self.current_question[1]}", fg="red")

        self.question_count += 1
        self.update_score_label()
        self.next_question()

    def update_score_label(self):
        self.score_label.config(text=f"Puntaje: {self.score}")

    def finish_quiz(self):
        if self.score >= 7:
            self.result_label.config(text=f"¡Felicidades! Puntaje final: {self.score}. Puedes salir del juego.", fg="blue")
            self.master.quit()  # Cierra la ventana si el puntaje es 7 o más
        else:
            self.result_label.config(text=f"Puntaje final: {self.score}. Necesitas 7 puntos para salir. Intenta de nuevo.", fg="orange")
        self.reset_quiz()

    def reset_quiz(self):
        self.score = 0
        self.question_count = 0
        self.questions.clear()
        self.subject_var.set("")

        # Reinicia la interfaz
        self.subject_label.pack()
        self.start_button.pack()
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()

        self.result_label.config(text="")
        self.score_label.config(text="Puntaje: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiSubjectQuiz(root)
    root.mainloop()
