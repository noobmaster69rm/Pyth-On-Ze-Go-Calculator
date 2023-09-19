# Alexander Shekhar Parke's (M00832048) and Vishek Ramgolam's (M00851334) Calculator

import tkinter as tk
import threading
from tkmacosx import Button
from PIL import Image, ImageTk
from math import *

# Defining buttons' characteristics instead of typing everything again
button_border_size = {
    'font': ('arial', 18),
    'borderwidth': 4,
    'highlightcolor': '#464645',
    'highlightbackground': '#464645',
    'width': 64,
    'height': 48
}


# Defining sin cos tan and their inverses
def fsin(arg):
    return sin(arg * rad)


def fcos(arg):
    return cos(arg * rad)


def ftan(arg):
    return tan(arg * rad)


def arcsin(arg):
    return deg * (asin(arg))


def arccos(arg):
    return deg * (acos(arg))


def arctan(arg):
    return deg * (atan(arg))


rad = 1
deg = 1


class Calculator:
    def __init__(self, master):
        # expression that will be displayed on screen
        self.expression = ""

        # to store data in memory
        self.recall = ""

        # to calculate and display answer (self.answer)
        self.sum_up = ""

        self.master = master

        # To convert input from text to string in order for calculation to be possible
        self.text_input = tk.StringVar()

        # First frame for the display screen
        screen_frame = tk.Frame(master,
                                width=580,
                                height=80,
                                bg='#30302f',
                                relief='flat')
        screen_frame.place(x=0)

        # Second frame for the entry box
        display_frame = tk.Entry(screen_frame,
                                 font=('arial', 32),
                                 width=580,
                                 bg='#30302f',
                                 fg='white',
                                 textvariable=self.text_input,
                                 relief='flat',
                                 borderwidth=0,
                                 highlightthickness=0)
        display_frame.place(x=0)

        # Third frame for button layout
        buttons_frame = tk.Frame(master,
                                 width=580,
                                 height=245,
                                 bg='#606060',
                                 relief='flat')
        buttons_frame.place(x=0, y=80)

        # Calculator's button placement row by row
        self.button_left_bracket = Button(buttons_frame,
                                          bg='#464645',
                                          fg='white',
                                          text="(",
                                          command=lambda: self.button_click('('),
                                          **button_border_size
                                          )
        self.button_left_bracket.place(x=0, y=0)

        self.button_right_bracket = Button(buttons_frame,
                                           bg='#464645',
                                           fg='white',
                                           text=")",
                                           command=lambda: self.button_click(')'),
                                           **button_border_size
                                           )
        self.button_right_bracket.place(x=64, y=0)

        self.button_sin = Button(buttons_frame,
                                 bg='#464645',
                                 fg='white',
                                 text="sin",
                                 command=lambda: self.button_click('fsin('),
                                 **button_border_size)
        self.button_sin.place(x=128, y=0)

        self.button_cos = Button(buttons_frame,
                                 bg='#464645',
                                 fg='white',
                                 text="cos",
                                 command=lambda: self.button_click('fcos('),
                                 **button_border_size)
        self.button_cos.place(x=192, y=0)

        self.button_tan = Button(buttons_frame,
                                 bg='#464645',
                                 fg='white',
                                 text="tan",
                                 command=lambda: self.button_click('ftan('),
                                 **button_border_size)
        self.button_tan.place(x=256, y=0)

        self.button_clear = Button(buttons_frame,
                                   bg='#Be2825',
                                   fg='white',
                                   text="AC",
                                   command=self.button_clear_all,
                                   **button_border_size)
        self.button_clear.place(x=320, y=0)

        self.button_change_sign = Button(buttons_frame,
                                         bg='#464645',
                                         fg='white',
                                         text="+/-",
                                         command=self.change_signs,
                                         **button_border_size)
        self.button_change_sign.place(x=384, y=0)

        delete_icon = Image.open('img.png')
        delete_icon = delete_icon.resize((64, 64), Image.ANTIALIAS)
        del_img = ImageTk.PhotoImage(delete_icon)
        self.button_delete = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    image=del_img,
                                    command=self.delete_button,
                                    **button_border_size)
        self.button_delete.place(x=448, y=0)

        self.button_divide = Button(buttons_frame,
                                    bg='#ff9f0b',
                                    fg='white',
                                    text="÷",
                                    command=lambda: self.button_click('/'),
                                    **button_border_size)
        self.button_divide.place(x=512, y=0)

        self.button_rad = Button(buttons_frame,
                                 bg='#464645',
                                 fg='white',
                                 text="Rad",
                                 command=self.convert_rad,
                                 activeforeground='orange',
                                 **button_border_size)
        self.button_rad.place(x=0, y=48)

        self.button_deg = Button(buttons_frame,
                                 bg='#464645',
                                 fg='white',
                                 text="Deg",
                                 command=self.convert_deg,
                                 activeforeground='red',
                                 **button_border_size)
        self.button_deg.place(x=64, y=48)

        self.button_arcsin = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="sinh",
                                    command=lambda: self.button_click('arcsin('),
                                    **button_border_size)
        self.button_arcsin.place(x=128, y=48)

        self.button_arccos = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="cosh",
                                    command=lambda: self.button_click('arccos('),
                                    **button_border_size)
        self.button_arccos.place(x=192, y=48)

        self.button_arctan = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="tanh",
                                    command=lambda: self.button_click('arctan('),
                                    **button_border_size)
        self.button_arctan.place(x=256, y=48)

        self.button_7 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="7",
                               command=lambda: self.button_click(7),
                               **button_border_size)
        self.button_7.place(x=320, y=48)

        self.button_8 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="8",
                               command=lambda: self.button_click(8),
                               **button_border_size)
        self.button_8.place(x=384, y=48)

        self.button_9 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="9",
                               command=lambda: self.button_click(9),
                               **button_border_size)
        self.button_9.place(x=448, y=48)

        self.button_multiply = Button(buttons_frame,
                                      bg='#ff9f0b',
                                      fg='white',
                                      text="x",
                                      command=lambda: self.button_click('*'),
                                      **button_border_size)
        self.button_multiply.place(x=512, y=48)

        self.button_1overx = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="⅟",
                                    command=lambda: self.button_click('1/'),
                                    **button_border_size)
        self.button_1overx.place(x=0, y=96)

        self.button_square = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="x²",
                                    command=lambda: self.button_click('**2'),
                                    **button_border_size)
        self.button_square.place(x=64, y=96)

        self.button_cube = Button(buttons_frame,
                                  bg='#464645',
                                  fg='white',
                                  text="x³",
                                  command=lambda: self.button_click('**3'),
                                  **button_border_size)
        self.button_cube.place(x=128, y=96)

        self.button_xpowern = Button(buttons_frame,
                                     bg='#464645',
                                     fg='white',
                                     text="xⁿ",
                                     command=lambda: self.button_click('**'),
                                     **button_border_size)
        self.button_xpowern.place(x=192, y=96)

        self.button_exponential = Button(buttons_frame,
                                         bg='#464645',
                                         fg='white',
                                         text="e",
                                         command=lambda: self.button_click('2.718281828459045'),
                                         **button_border_size)
        self.button_exponential.place(x=256, y=96)

        self.button_4 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="4",
                               command=lambda: self.button_click(4),
                               **button_border_size)
        self.button_4.place(x=320, y=96)

        self.button_5 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="5",
                               command=lambda: self.button_click(5),
                               **button_border_size)
        self.button_5.place(x=384, y=96)

        self.button_6 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="6",
                               command=lambda: self.button_click(6),
                               **button_border_size)
        self.button_6.place(x=448, y=96)

        self.button_minus = Button(buttons_frame,
                                   bg='#ff9f0b',
                                   fg='white',
                                   text="-",
                                   command=lambda: self.button_click('-'),
                                   **button_border_size)
        self.button_minus.place(x=512, y=96)

        self.button_factorial = Button(buttons_frame,
                                       bg='#464645',
                                       fg='white',
                                       text="x!",
                                       command=lambda: self.button_click('factorial('),
                                       **button_border_size)
        self.button_factorial.place(x=0, y=144)

        self.button_squareroot = Button(buttons_frame,
                                        bg='#464645',
                                        fg='white',
                                        text="√",
                                        command=lambda: self.button_click('sqrt('),
                                        **button_border_size)
        self.button_squareroot.place(x=64, y=144)

        self.button_cuberoot = Button(buttons_frame,
                                      bg='#464645',
                                      fg='white',
                                      text="3√",
                                      command=lambda: self.button_click('**(1/3)'),
                                      **button_border_size)
        self.button_cuberoot.place(x=128, y=144)

        self.button_root = Button(buttons_frame,
                                  bg='#464645',
                                  fg='white',
                                  text="y√x",
                                  command=lambda: self.button_click('**(1/'),
                                  **button_border_size
                                  )
        self.button_root.place(x=192, y=144)

        self.button_MC = Button(buttons_frame,
                                bg='#464645',
                                fg='white',
                                text="MC",
                                command=lambda: self.memory_clear(),
                                **button_border_size)
        self.button_MC.place(x=256, y=144)

        self.button_1 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="1",
                               command=lambda: self.button_click(1),
                               **button_border_size)
        self.button_1.place(x=320, y=144)

        self.button_2 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="2",
                               command=lambda: self.button_click(2),
                               **button_border_size)
        self.button_2.place(x=384, y=144)

        self.button_3 = Button(buttons_frame,
                               bg='#7a7b7a',
                               fg='white',
                               text="3",
                               command=lambda: self.button_click(3),
                               **button_border_size)
        self.button_3.place(x=448, y=144)

        self.button_minus = Button(buttons_frame,
                                   bg='#ff9f0b',
                                   fg='white',
                                   text="+",
                                   command=lambda: self.button_click('+'),
                                   **button_border_size)
        self.button_minus.place(x=512, y=144)

        self.button_ln = Button(buttons_frame,
                                bg='#464645',
                                fg='white',
                                text="ln",
                                command=lambda: self.button_click('log('),
                                **button_border_size)
        self.button_ln.place(x=0, y=192)

        self.button_10powerx = Button(buttons_frame,
                                      bg='#464645',
                                      fg='white',
                                      text="10ˣ",
                                      command=lambda: self.button_click('10**'),
                                      **button_border_size)
        self.button_10powerx.place(x=64, y=192)

        self.button_pi = Button(buttons_frame,
                                bg='#464645',
                                fg='white',
                                text="π",
                                command=lambda: self.button_click('22/7'),
                                **button_border_size)
        self.button_pi.place(x=128, y=192)

        self.button_comma = Button(buttons_frame,
                                   bg='#464645',
                                   fg='white',
                                   text=",",
                                   command=lambda: self.button_click(','),
                                   **button_border_size)
        self.button_comma.place(x=192, y=192)

        self.button_answer = Button(buttons_frame,
                                    bg='#464645',
                                    fg='white',
                                    text="ans",
                                    command=self._answer,
                                    **button_border_size)
        self.button_answer.place(x=256, y=192)

        self.button_0 = Button(buttons_frame,
                               width=128,
                               height=48,
                               bg='#7a7b7a',
                               fg='white',
                               borderwidth=3,
                               highlightcolor='#464645',
                               highlightbackground='#464645',
                               text="0",
                               command=lambda: self.button_click(0))
        self.button_0.place(x=320, y=192)

        self.button_decimal = Button(buttons_frame,
                                     bg='#7a7b7a',
                                     fg='white',
                                     text=".",
                                     command=lambda: self.button_click('.'),
                                     **button_border_size)
        self.button_decimal.place(x=448, y=192)

        self.equal_button = Button(buttons_frame,
                                   bg='#ff9f0b',
                                   fg='white',
                                   text="=",
                                   command=self.button_equal,
                                   **button_border_size)
        self.equal_button.place(x=512, y=192)

    # inputting the values (defining what happens when the buttons are clicked)
    def button_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    # Remove displayed string from the screen
    def button_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    # Delete last index of the displayed value
    def delete_button(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    # Adding negative sign in front of displayed value
    def change_signs(self):
        self.expression = '-' + self.expression
        self.text_input.set(self.expression)

    # Functions to allow using either degrees or radians
    def convert_deg(self):
        global rad
        global deg
        rad = (22 / 7) / 180
        deg = 180 / (22 / 7)
        self.button_rad["foreground"] = 'white'
        self.button_deg["foreground"] = 'light green'

    def convert_rad(self):
        global rad
        global deg
        rad = 1
        deg = 1
        self.button_rad["foreground"] = 'red'
        self.button_deg["foreground"] = 'white'

    # Clearing memory of calculator
    def memory_clear(self):
        self.recall = ""

    # Answer button
    def _answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    # Converting input to string and then calculate the value
    def button_equal(self):
        if self.expression == "":
            self.text_input.set(self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)
            self.sum_up = str(eval(self.expression))
            self.text_input.set(self.sum_up)
            self.expression = self.sum_up

        self.recall = self.recall + ' ' + self.expression

    # Creating Threads to run functions simultaneously

def create_gui():
    cal = tk.Tk()
    Calculator(cal)
    cal.geometry("580x325")
    cal.title("CST1500 Calculator")
    cal.iconbitmap("img_1.icns")

    # making the window translucent
    cal.attributes('-alpha', 0.95)
    cal.mainloop()


create_gui()
