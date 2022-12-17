from tkinter import *
import turtle

window = Tk()

window.title("My secong of third GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

general_text = "I'm a label"

# def button_clicked():
#     msg = input1.get()
#
#     my_label['text'] = msg
#     print('I got clicked')
#     for item in corner_labels:
#         item.config(text=msg)


# PACK
# packing stacks all gadgets with lack of precision, just stack them
# my_label = Label(text=general_text, font=('Arial', 24, 'bold'))
# my_label.pack(expand=True)  # side= "left","right", "bottom", "top"
#
# input1 = Entry(width=10)
# input1.pack()
#
# button = Button(text='click me', command=button_clicked)
# button.pack()

# # PLACE
# # the place method allows precise placing in the tkinter windoe
# my_label2 = Label(text=general_text)
# my_label2.place(x=0, y=0)
# my_label3 = Label(text=general_text)
# my_label3.place(x=400, y=0)
# my_label4 = Label(text=general_text)
# my_label4.place(x=400, y=250)
# my_label5 = Label(text=general_text)
# my_label5.place(x=0, y=250)
#
# corner_labels = [my_label2, my_label3, my_label4, my_label5]

# GRID
# grid system is relative to other components
# NOTE: you CAN NOT mix grid and pack, but you can use place and grid (they don't interact).
grid_label1 = Label(text='victor')
grid_label1.grid(column=1, row=1)
grid_label1.config(padx=50, pady=50)
button = Button(text='victor')
button.grid(column=2, row=2)
button.config(padx=50, pady=50)
new_button = Button(text='victor')
new_button.grid(column=3, row=1)
entry = Entry(text='victor')
entry.grid(column=4, row=3) # entry cant be padded
window.mainloop()

# advance arguments *args, **kwargs

tim = turtle.Turtle()
tim.write("vitisman")


def adds(*args):
    suma = 0
    sentence = ""
    for item in args:
        if type(item) == int:
            suma += item
        else:
            sentence += item
    print(f"{suma} {sentence}")


adds(1, 2, 3, "tequila!!")


class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs['make'] #  this way creates errors if not specified
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')
        self.seats = kwargs.get('seats')


my_car = Car(make='Nissan', model='GT-R')
print(my_car.colour)
