import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title('tictactoe game')
window.geometry('500x700+300+0')
window.resizable(0,0)

name = tkinter.Frame(window)
namelabel = tkinter.Label(name, text = 'TIC-TAC-TOE', bg = '#bbbbbb', fg = '#2222ff', font = ('Cambria', 50, 'bold'))
namelabel.pack()
name.grid(row = 1, column = 1, pady = 5)



testing = True
count = 0
xscore = 0
yscore = 0


def update_xscore(wd):
    wd.configure(text=xscore)

def update_yscore(wd):
    wd.configure(text=yscore)

def res():
    global xscore, yscore
    clear()
    xscore = 0
    yscore = 0
    scoreX.configure(text = 0)
    scoreO.configure(text = 0)
    
def clear():
    global count
    for i in [one, two, three, four, five,six,seven,eight,nine]:
        i['text'] = ''
        i.configure(state = 'normal', bg = '#990000')
    count = 0
    testing = True
    
def check():
    global xscore, yscore
    if count == 9:
        messagebox.showinfo('tic tac toe', 'no one wins, pls, restart')
        clear()
        
    elif  one['text'] == 'X' and two['text'] == 'X' and three['text'] == 'X':
        one.config(bg = 'white', fg = '#ffffff')
        two.config(bg = 'yellow', fg = '#ffffff')
        three.config(bg = '#0000bb', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif four['text'] == 'X' and five['text'] == 'X' and six['text'] == 'X' :
        four.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        six.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif seven['text'] == 'X' and eight['text'] == 'X' and nine['text'] == 'X' :
        seven.config(bg = 'white', fg = '#ffffff')
        eight.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif one['text'] == 'X' and four['text'] == 'X' and seven['text']== 'X' :
        one.config(bg = 'white', fg = '#ffffff')
        four.config(bg = 'yellow', fg = '#ffffff')
        seven.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif two['text'] == 'X' and five['text'] == 'X' and eight['text'] == 'X':
        two.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        eight.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif three['text'] == 'X' and six['text'] == 'X' and nine['text'] == 'X':
        three.config(bg = 'white', fg = '#ffffff')
        six.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif one['text'] == 'X' and five['text'] == 'X' and nine['text'] == 'X' :
        one.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
    elif three['text'] == 'X' and five['text'] == 'X' and seven['text'] == 'X':
        three.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        seven.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
        update_xscore(scoreX)
        
    elif one['text'] == 'O' and two['text'] == 'O' and three['text'] == 'O':
        one.config(bg = 'red', fg = '#ffffff')
        two.config(bg = 'red', fg = '#ffffff')
        three.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif four['text'] == 'O' and five['text'] == 'O' and six['text'] == 'O' :
        four.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        six.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif seven['text'] == 'O' and eight['text'] == 'O' and nine['text'] == 'O' :
        seven.config(bg = 'white', fg = '#ffffff')
        eight.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif one['text'] == 'O' and four['text'] == 'O' and seven['text']== 'O' :
        one.config(bg = 'white', fg = '#ffffff')
        four.config(bg = 'yellow', fg = '#ffffff')
        seven.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif two['text'] == 'O' and five['text'] == 'O' and eight['text'] == 'O':
        two.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        eight.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif three['text'] == 'O' and six['text'] == 'O' and nine['text'] == 'O':
        three.config(bg = 'white', fg = '#ffffff')
        six.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif one['text'] == 'O' and five['text'] == 'O' and nine['text'] == 'O' :
        one.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        nine.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)
    elif three['text'] == 'O' and five['text'] == 'O' and seven['text'] == 'O':
        three.config(bg = 'white', fg = '#ffffff')
        five.config(bg = 'yellow', fg = '#ffffff')
        seven.config(bg = 'blue', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        yscore += 1
        clear()
        update_yscore(scoreO)


def click(button): # function to alternate btw X and O
    global testing,count
    if testing:
        button['text'] = 'X'
        button.configure(state = 'disabled')
        testing = False
        count +=1
        check()
    else:
        button['text'] = 'O'
        button.configure(state = 'disabled')
        testing = True
        count +=1
        check()

#adding the nine grid buttons
widthsize = 4
heightsize = 1
background = '#990000'
foreground = 'white'
lettering = ('Cambria', 50, 'bold')
buttons = tkinter.Frame(window)
one = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(one))
two = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(two))
three = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(three))
four = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(four))
five = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(five))
six = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(six))
seven = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(seven))
eight = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(eight))
nine = tkinter.Button(buttons, text = '', width = widthsize, height = heightsize,
                     bg = background, fg = foreground, font = lettering, command = lambda: click(nine))

one.grid(row = 0, column = 0)
two.grid(row = 0, column = 1)
three.grid(row = 0, column = 2)
four.grid(row = 1, column = 0)
five.grid(row = 1, column = 1)
six.grid(row = 1, column = 2)
seven.grid(row = 2, column = 0)
eight.grid(row = 2, column = 1)
nine.grid(row = 2, column = 2)

buttons.grid(row = 2, column = 1)


scoreboard = tkinter.Frame()
labelO = tkinter.Label(scoreboard, text = 'O\'s current score:       ', bg = 'white', fg = 'blue',
                       font = ('Calibri', 30, 'bold'))
labelX = tkinter.Label(scoreboard, text = 'X\'s current score:       ', bg = 'white', fg = 'blue',
                       font = ('Calibri', 30, 'bold'))
scoreO = tkinter.Label(scoreboard, text = yscore, bg = 'white', fg = 'blue',
                       font = ('Calibri', 30, 'bold'))
scoreX = tkinter.Label(scoreboard, text = xscore, bg = 'white', fg = 'blue',
                       font = ('Calibri', 30, 'bold'))
labelO.grid(row = 0, column = 0)
labelX.grid(row = 1, column = 0)
scoreO.grid(row = 0, column = 1)
scoreX.grid(row = 1, column = 1)
scoreboard.grid(row = 3, column = 1)


buttons = tkinter.Frame()
reset = tkinter.Button(buttons, text = 'reset', font = ('calibri',20, 'bold'), command = res, width = 15, bg = 'yellow', fg = '#9900ff').grid()
buttons.grid(row = 4, column = 1)
