from tkinter import *

class Calculator:
    def __init__(self, master):
        master.title("Calculator made by Sharif")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        self.create_widgets(master)

    def create_widgets(self, master):
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50),
            ('1', 0, 125), ('2', 90, 125), ('3', 180, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200),
            ('7', 0, 275), ('8', 90, 275), ('9', 180, 275),
            ('0', 90, 350), ('.', 180, 350), ('+', 270, 275),
            ('-', 270, 200), ('/', 270, 50), ('x', 270, 125),
            ('=', 270, 350), ('C', 0, 350)
        ]

        for (text, x, y) in buttons:
            if text == "=":
                Button(width=11, height=4, text=text, relief='flat', bg='lightblue', command=self.solve).place(x=x, y=y)
            elif text == "C":
                Button(width=11, height=4, text=text, relief='flat', bg='white', command=self.clear).place(x=x, y=y)
            else:
                Button(width=11, height=4, text=text, relief='flat', bg='white', command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        
        if value in ('+', '-', '*', '/', '%') and self.entry_value[-1:] in ('+', '-', '*', '/', '%'):
            return

        
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value.replace('x', '*')) 
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")


root = Tk()
calculator = Calculator(root)

root.mainloop()
