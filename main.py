from tkinter import *

def convert():
    miles = entry.get()
    if miles.isdigit():
        km = round(float(miles) * 1.60934, 2)
        label_result.config(text=f"{km} km")
    else:
        label_result.config(text="Enter a number")

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Labels
label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equals = Label(text="is equal to")
label_equals.grid(row=1, column=0)

label_result = Label(text="0 km")
label_result.grid(row=1, column=1)

label_km = Label(text="Kilometers")
label_km.grid(row=1, column=2)

# Button
button = Button(text="Convert", command=convert)
button.grid(row=2, column=1)

window.mainloop()
