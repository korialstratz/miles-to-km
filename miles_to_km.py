from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.title("Miles to km")
window.config(padx=20, pady=20)


def conversion():
    mile = int(entry.get())
    km = mile * 1.609344
    km = "{:.2f}".format(km)
    conversion_label["text"] = km


entry = Entry(width=6)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)

conversion_label = Label(text="0")
conversion_label.grid(column=1, row=1)
conversion_label.config(padx=5, pady=5)

km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

convert_button = Button(text="Convert", command=conversion)
convert_button.grid(column=1, row=2)
convert_button.config(padx=5, pady=5)

window.mainloop()
