import tkinter as tk
from math import sqrt
window = tk.Tk()
window.title('Calculator')
window.configure(bg = '#bfbfbf')
window.rowconfigure([1,2,3,4,5], pad = 60)
window.geometry('500x600')
        
def equal():
    result = int(eval(display.get()))
    display.delete(0, 'end')
    display.insert('end', result)
    

def square():
    try:
        result = int(display.get() ** 2)
        display.delete(0, 'end')
        display.insert('end', result)
    except:
        pass
        

def plusminus():
    try:
        x = int(display.get()) * -1
        display.delete(0, 'end')
        display.insert('end', x)
    except:
        pass

def root():
    num = int(float(display.get()))
    try:
        display.delete(0, 'end')
        display.insert(0, sqrt(int(num)))
    except:
        display.delete(0, 'end')
        display.configure(fg = 'red')
        display.insert(0, 'error occured')

'''logo = tk.PhotoImage(file = 'logo.png')
tk.Label(photo = logo, height = 20, width = 10).pack(side = 'top')'''
        
topic = tk.Label(window, text = 'Simple Calculator', bg = '#bfbfbf', fg = 'black', font = ('Cambria', 20)).grid(row = 0, column = 1, pady = 10)

display = tk.Entry(window, textvariable = 0, text = 0, borderwidth = 0, font = ('Arial', 30, 'bold'),   bg = '#bfbfbf',  fg = 'black')
display.grid(row = 1, column = 1)


Buttons = tk.Frame(window, bg = '#bfbfbf')
size = '8'
squared = tk.Button(Buttons, text = 'x^2', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat', command = lambda: display.insert('end', 1)).grid(row = 4, column = 1)
    
btn1 = tk.Button(Buttons, text = '1', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat', command = lambda: display.insert('end', 1)).grid(row = 4, column = 1)
btn2 = tk.Button(Buttons, text = '2', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat', command = lambda: display.insert('end', 2)).grid(row = 4, column = 2)
btn3 = tk.Button(Buttons, text = '3', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 3)).grid(row = 4, column = 3)

btn4 = tk.Button(Buttons, text = '4', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 4)).grid(row = 3, column = 1)
btn5 = tk.Button(Buttons, text = '5', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 5)).grid(row = 3, column = 2)
btn6 = tk.Button(Buttons, text = '6', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat', command = lambda: display.insert('end', 6)).grid(row = 3, column = 3)
btn7 = tk.Button(Buttons, text = '7', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 7)).grid(row = 2, column = 1)

btn8 = tk.Button(Buttons, text = '8', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 8)).grid(row = 2, column = 2)
btn9 = tk.Button(Buttons, text = '9', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat' ,command = lambda: display.insert('end', 9)).grid(row = 2, column = 3)
btn0 = tk.Button(Buttons, text = '0', font = ('Calibri', 20, 'bold'), fg = 'black', bg = 'white', width = size, relief = 'flat', command = lambda: display.insert('end', 0)).grid(row = 5, column = 2)

btnplus = tk.Button(Buttons, text = '+', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.insert('end', '+')).grid(row = 4, column = 4)
btnequal = tk.Button(Buttons, text = '=', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = equal).grid(row = 5, column = 4)
btnsubtract = tk.Button(Buttons, text = '-', font = ('Calibri', 20, 'bold'), bg = '#dddddd', fg = 'black', width = size, relief = 'flat', command = lambda: display.insert('end', '-')).grid(row = 3, column = 4)
btndivide = tk.Button(Buttons, text = '/', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.insert('end', '/')).grid(row = 1, column = 4)
btnmultiply = tk.Button(Buttons, text = 'x', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.insert('end', '*')).grid(row = 2, column = 4)
btnreset = tk.Button(Buttons, text = 'C', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.delete(0, 'end')).grid(row = 1, column = 2)
btndel = tk.Button(Buttons, text = 'del', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.delete(len(display.get()) -1, 'end')).grid(row = 1, column = 1)
btnplusminus = tk.Button(Buttons, text = '+/_', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = plusminus).grid(row = 1, column = 3)
btnpoint = tk.Button(Buttons, text = '.', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = lambda: display.insert('end', '.')).grid(row = 5, column = 3)
btnsqrt = tk.Button(Buttons, text = '\u221A', font = ('Calibri', 20), fg = 'black', bg = '#dddddd', width = size, relief = 'flat', command = root ).grid(row = 5, column = 1)

Buttons.rowconfigure([1,2,3,4,5], pad = 5)
Buttons.columnconfigure([1,2,3,4,5], pad = 5)
Buttons.grid(row = 2, column = 1)

tk.mainloop()



