import tkinter as tk


def handle_button_press(event):
    button_text = event.widget.cget("text")
    current_text = display.get()

    if button_text == "C":
        display.delete(0, tk.END)
    elif button_text == "=":
        try:
            result = eval(current_text)  # Evaluate the expression
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, button_text)


# Create the main window.
window = tk.Tk()
window.title("Calculator")

display = tk.Entry(window, font=("Arial", 24), bd=10, relief="ridge")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons and use the grid geometry manager.
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
    ("C", 5, 0, 4),
]

for text, row, column, *args in buttons:
    button = tk.Button(window, text=text, font=("Arial", 18), width=5, height=2)
    button.grid(
        row=row, column=column, padx=5, pady=5, columnspan=args[0] if args else 1
    )
    button.bind("<Button-1>", handle_button_press)

# Start the event loop.
window.mainloop()
