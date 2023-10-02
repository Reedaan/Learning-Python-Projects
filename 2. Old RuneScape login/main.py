import random
import tkinter as tk

window = tk.Tk()
window.title("Old runescape bank login")


def shuffle(button):
    random.shuffle(POSITIONS)
    for number, position in enumerate(POSITIONS):
        button_dict[f"button_{number}"].grid(row=position[0], column=position[1])
    pressed_list.append(button)
    pressed_label.config(text=pressed_list)
    if len(pressed_list) >= 4:
        pressed_list.clear()
        pressed_label.config(text="Incorrect password")


pressed_label = tk.Label(text="", font=("Arial"))
pressed_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
pressed_list = []

button_dict = {}

# Grid positions row:column
POSITIONS = [
    (3, 0),
    (3, 1),
    (3, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (1, 0),
    (1, 1),
    (1, 2),
    (4, 1),
]

# Creating a dictionary of button objects, example: button_0 = "0"
for number in range(10):
    button = button_dict["button_{0}".format(number)] = tk.Button(
        text=f"{number}",
        height=2,
        width=2,
        font=("Arial", 12),
        command=lambda button=number: shuffle(button),
    )

# Starting the program without using the function, so it correctly counts pressed numbers
random.shuffle(POSITIONS)
for number, position in enumerate(POSITIONS):
    button_dict[f"button_{number}"].grid(
        row=position[0], column=position[1], padx=5, pady=5, sticky="nsew"
    )

# Make all columns stretch equally
for i in range(3):
    window.columnconfigure(i, weight=1)

# Make the window resizable
window.rowconfigure(0, weight=1)

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_reqwidth()) // 2
y = (screen_height - window.winfo_reqheight()) // 2
window.geometry("+{}+{}".format(x, y))

window.mainloop()
