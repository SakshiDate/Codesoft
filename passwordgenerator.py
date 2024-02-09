import string
import random
from tkinter import *

def generate_password():
    password_strength = choice.get()
    password_length = int(val.get())

    if password_strength == 1:
        characters = string.ascii_letters
    elif password_strength == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    result.config(text="Generated Password: " + generated_password)

root = Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg='lightgray')

frame_strength = Frame(root, bg='blue')
frame_strength.pack(pady=10)

label_strength = Label(frame_strength, text="Select Password Strength", fg='white', bg='blue',
                        font=('Helvetica', 12))
label_strength.pack(pady=5)

choice = IntVar()
rb1 = Radiobutton(frame_strength, text="Weak (Letters Only)", variable=choice, value=1)
rb2 = Radiobutton(frame_strength, text="Medium (Letters + Numbers)", variable=choice, value=2)
rb3 = Radiobutton(frame_strength, text="Strong (Letters + Numbers + Symbols)", variable=choice, value=3)
rb1.pack()
rb2.pack()
rb3.pack()

frame_length = Frame(root, bg='red')
frame_length.pack(pady=10)

label_length = Label(frame_length, text="Enter Password Length", fg='white', bg='red',
                     font=('Helvetica', 12))
label_length.pack(pady=5)

val = StringVar()
password_length_entry = Entry(frame_length, textvariable=val)
password_length_entry.pack(pady=5)

generate_button = Button(root, text="Generate Password", command=generate_password, bg='green', fg='white',
                         font=('Helvetica', 12))
generate_button.pack(pady=10)

result = Label(root, text="", font=('Helvetica', 12))
result.pack()

root.mainloop()
