import tkinter as tk

def click_button(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=10, command=lambda t=text: click_button(t) if t != "=" else calculate_result())
    button.grid(row=row, column=col)

clear_button = tk.Button(window, text="C", padx=20, pady=10, command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4)

window.mainloop()