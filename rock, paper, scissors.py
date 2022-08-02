import tkinter
from random import randint
import time
screen = tkinter.Tk()
while True:
    choices = ['rock', 'paper', 'scissors']
    y = randint(0, 2)
    p = choices[y]
    x = input('enter your choice: ')
    print('computer played ' + p)
    if x == p:
        print('same value, counted as draw, play again')
    elif x == 'rock' and p == 'paper':
        print('ouch! you loose, computer wins, play again')
    elif x == 'paper' and p == 'rock':
        tkinter.Tk()
        tkinter.Label(text="You win, hurray!!!", bg="#ff2200", fg="#000045").grid(row=2, column=5)
        print('you won')
    elif x == 'paper' and p == 'scissors':
        print('ouch! computer cut you,  you loose, computer wins, play again')
    elif x == 'scissors' and p == 'paper':
        tkinter.Label(screen, text="You win, hurray!!!", bg="#ff2200", fg="#000045").grid(row=2, column=5)
        break
        tkinter.mainloop()
    elif x == 'scissors' and p == 'rock':
        print('ouch! you loose, computer wins, play again')
    elif x == 'rock' and p == 'scissors':
        print('you won')
    elif x == 'end':
        break
    else:
        print('invalid value')
        
