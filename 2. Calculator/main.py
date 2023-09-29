import tkinter as tk
import random
#TODO
#Add basic calculator functions
#Saving the result to a variable
#tkinter GUI
#GUI Layout
#Add functionality 
#
#
#
#
#
#
#

window = tk.Tk()
window.title("Old runescape bank login")

display = tk.Label(text="")

display.grid(row=0, columnspan=3)

button_dict = {}
#Grid positions row:column
positions = [(3,0), (3,1), (3,2), (2,0), (2,1), (2,2), (1,0), (1,1), (1,2), (4,1)]
#Creating a dictionary of button objects, example: button_0 = "0"}
for number in range(10):
    button_dict["button_{0}".format(number)] = tk.Button(text=f"{number}")

for key in button_dict:
    button_dict.get(key).grid(positions[0[0]], positions[0[1]])

# for object in button_dict:
#     button_dict.get(object).grid(row=3, column=0)

# button_1 = tk.Button(text="1")
# button_2 = tk.Button(text="2")
# button_3 = tk.Button(text="3")
# button_4 = tk.Button(text="4")
# button_5 = tk.Button(text="5")
# button_6 = tk.Button(text="6")
# button_7 = tk.Button(text="7")
# button_8 = tk.Button(text="8")
# button_9 = tk.Button(text="9")
# button_0 = tk.Button(text="0")

# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
# button_0.grid(row=4, column=1)


window.mainloop()