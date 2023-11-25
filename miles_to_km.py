from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.689
    label_3.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
# window.minsize(400, 200)
window.config(padx=20, pady=20)

input = Entry(width=5)
input.grid(row=0, column=1)

label = Label(text="Miles", font=("Arial", 14, "bold"))
label.grid(row=0, column=2)

label_2 = Label(text="is equal to", font=("Arial", 14, "bold"))
label_2.grid(row=1, column=0)

label_3 = Label(text="0", font=("Arial", 14, "bold"))
label_3.grid(row=1, column=1)

label_4 = Label(text="Km", font=("Arial", 14, "bold"))
label_4.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()