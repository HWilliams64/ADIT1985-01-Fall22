from tkinter import *

total = 0

def click():
    global total
    total += 1
    print(f"The button was clicked: {total}")

window = Tk()

window.title("Example Application")

window.geometry("500x300")

label = Label(window, text='Hello Python Developers', font=("Arial Bold", 20))

label.grid(column=0, row=0)

button = Button(window, text="Click me", command=click)

button.grid(column=0, row=1)

window.mainloop()
