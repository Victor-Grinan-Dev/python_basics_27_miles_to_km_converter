from tkinter import *

window = Tk()
window.title('km to miles')


def calculate():
    req = entry.get()
    entry.delete(0, END)
    result = float(req) * 1.60934

    label_result['text'] = f'{result:.2f}'


entry = Entry(text='0')
entry.grid(row=1, column=2)
label_miles = Label(text='Miles')
label_miles.grid(row=1, column=3)
label_equal = Label(text='is equal to:')
label_equal.grid(row=2, column=1)
label_result = Label(text=0)
label_result.grid(row=2, column=2)
label_km = Label(text='Km')
label_km.grid(row=2, column=3)
button = Button(text='Calculate', command=calculate)
button.grid(row=3, column=2)

window.mainloop()
