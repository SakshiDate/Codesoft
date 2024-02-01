import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

root = tk.Tk()
root.title("Fancy Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result = tk.StringVar()
result.set("Result will be displayed here.")

result_label = tk.Label(root, textvariable=result, font=('Arial', 12), pady=10)
result_label.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

def button_click(event):
    if event.widget.cget("text") == "=":
        evaluate_expression()
    else:
        current_text = entry.get()
        new_text = current_text + event.widget.cget("text")
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

row_val = 2
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 12), bg='lightgray', fg='black')
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", button_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text="Clear", padx=20, pady=20, font=('Arial', 12), bg='tomato', fg='white', command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=row_val, column=col_val, padx=5, pady=5)

root.mainloop()
