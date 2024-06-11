from tkinter import *

def button_clicked():
    new_text = float(input.get()) * 1.609
    conversion.config(text=f"{new_text}")

window = Tk()
window.title("Miles to Km Conversion")
window.minsize(width=300, height=50)
window.config(padx=40,pady=15)

#Labels
is_equal_to = Label(text="is equal to")
is_equal_to.config(padx=5,pady=0)
# my_label.config(padx=10,pady=10)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.place(x=20, y=20)
is_equal_to.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=3, row=0)
miles.config(padx=5,pady=0)

conversion = Label(text="0")
conversion.grid(column=2, row=1)

km = Label(text="Km")
km.grid(column=3, row=1)
km.config(padx=10,pady=5)

#Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)
button.config(padx=5,pady=0)

#Entry

input = Entry(width=7)
input.grid(column=2, row=0)




window.mainloop()