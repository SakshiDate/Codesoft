import tkinter as tk
from tkinter import messagebox
import random

questions = [
    {"question": "What is the capital of India?", "options": ["London", "New Delhi", "Dubai", "Dhaka"], "correct_answer": "New Delhi"},
    {"question": "Which planet is the largest planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "correct_answer": "Jupiter"},
    {"question": "Which animal belongs to aquatic life?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "correct_answer": "Blue Whale"},
    {"question": "What is the capital of America?", "options": ["Beijing", "Tokyo", "Seoul", "Washington D.C"], "correct_answer": "Washington D.C"},
    {"question": "Which gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], "correct_answer": "Carbon Dioxide"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.root.config(bg="grey")

        self.score = 0
        self.current_question = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="grey", fg="white")
        self.question_label.pack(pady=15)
        
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        
        for i in range(4):
            radio_btn = tk.Radiobutton(root, text="", variable=self.radio_var, font=("Helvetica", 12), value=i, bg="grey", fg="white")
            self.radio_buttons.append(radio_btn)
            radio_btn.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", font=("Helvetica", 14), command=self.next_question, bg="green", fg="white")
        self.next_button.pack(pady=20)
        
        self.show_question()
    
    def show_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=f"Question {self.current_question + 1}: {q['question']}")
            options = q["options"]
            for i in range(4):
                self.radio_buttons[i].config(text=options[i])
            self.radio_var.set(None)
        else:
            self.show_result()
    
    def next_question(self):
        if self.current_question < len(questions):
            user_answer = self.radio_var.get()
            if user_answer is not None:
                user_answer = int(user_answer)
                q = questions[self.current_question]
                if q["options"][user_answer] == q["correct_answer"]:
                    self.score += 1
                self.current_question += 1
                self.show_question()
            else:
                messagebox.showwarning("Warning", "Please select an option before moving to the next question.")
        else:
            self.show_result()
    
    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You got {self.score}/{len(questions)} questions correct!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
