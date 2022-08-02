import tkinter as tk
top = tk.Tk()
top.rowconfigure([1, 3], weight = 5, minsize  = 50)
top.columnconfigure([1,3], weight = 5, minsize = 50)
L1 = tk.Label(top, text="My calculator",).grid(row=0, column=1)
L2 = tk.Label(top, text="Number 1",).grid(row=1, column=0)
L3 =tk.Label(top, text="Number 2",).grid(row=3, column=0)
L4 = tk.Label(top, text="Operator",).grid(row=2, column=0)
L4 = tk.Label(top, text="Answer")
L4.grid(row=4, column=0)
E1=tk.Entry(top,bd=1)
E1.grid(row=1, column=1)
E2=tk.Entry(top,bd=1)
E2.grid(row=2, column=1)
E3=tk.Entry(top,bd=1)
E3.grid(row=3, column=1)
E4=tk.Label(top,bd=1, background = 'blue', foreground = 'white')
E4.grid(row=4, column=1)
def process():
    try:
        number1=E1.get()
        number2=E3.get()
        operator=E2.get()
        number1=int(number1)
        number2=int(number2)
        if operator == '+':
            answer=number1 + number2
        elif operator == '-':
            answer=number1 - number2
        elif operator == '*':
            answer=number1 * number2
        elif operator == '/':
            answer=number1 / number2
        E4['text'] =f'The answer is {answer}'
    except:
        E4['text'] =f'Check your input, error occured'
B=tk.Button(top, text="calculate", command=process).grid(row=5,column=1,)
end=tk.Button(top, text="quit calculator", command=top.destroy).grid(row=6,column=1,)
tk.mainloop
