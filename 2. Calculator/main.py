import tkinter as tk
import random
#TODO getting hold of text from pressed button
#

window = tk.Tk()
window.title("Old runescape bank login")

def get_text():
    print()

def shuffle(): 
    random.shuffle(POSITIONS)
    for number, position in enumerate(POSITIONS):
        button_dict[f"button_{number}"].grid(row=position[0], column=position[1])    

pressed_label = tk.Label(text="")
pressed_label.grid(row=0, columnspan=3)

button_dict = {}

#Grid positions row:column
POSITIONS = [(3,0), (3,1), (3,2), (2,0), (2,1), (2,2), (1,0), (1,1), (1,2), (4,1)]

#Creating a dictionary of button objects, example: button_0 = "0"}
for number in range(10):
    button = button_dict["button_{0}".format(number)] = tk.Button(text=f"{number}", command=shuffle)

shuffle()

window.mainloop()