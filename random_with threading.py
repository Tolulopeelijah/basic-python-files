import tkinter as tk
import time
import threading
screen = tk.Tk()
screen.geometry('800x400')
screen.configure(bg = 'blue', padx = 50, pady = 50)
screen.title('3 loops with threading')

def start():
    first.start()
    second.start()
    third.start()
    
def dummy(lbl, starting_point, ctime):
    while True:
        time.sleep(ctime)
        if starting_point > 999:
            starting_point = 111
        else:
            starting_point += 1
        st = str(starting_point)

        lbl.config(text = st)
        screen.update()
        
label1 = tk.Label(screen, text = '111', fg='black', bg = 'silver', font = ('arial', 30, 'bold'), height = 2, width = 6)
label1.grid(padx = 10, row = 0, column = 0)
label2 = tk.Label(screen, text = '111', fg='black', bg = 'silver', font = ('arial', 30, 'bold'), height = 2, width = 6)
label2.grid(padx = 10, row = 0, column = 1)
label3 = tk.Label(screen, text = '111', fg='black', bg = 'silver', font = ('arial', 30, 'bold'), height = 2, width = 6)
label3.grid(padx = 10, row = 0, column = 2)  
btn = tk.Button(screen, fg='white', bg = 'red', height = 2, width = 6, text = 'start', font = ('arial', 10, 'bold'), command = start)
btn.grid(row = 1, column = 1, pady = 20)

def start():
    first.start()
    second.start()
    third.start()


ctime = 0.005
first = threading.Thread(target = dummy, args = [label1, 111, ctime])
second = threading.Thread(target = dummy, args = [label2, 232, ctime])
third = threading.Thread(target = dummy, args = [label3, 779, ctime])


screen.mainloop()
