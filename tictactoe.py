from tkinter import messagebox
import tkinter
window = tkinter.Tk()
window.geometry('600x700')
window.resizable(0, 0)
window.rowconfigure([1,2,3,4,5],  pad = 50)
t = tkinter.StringVar()

addtitle = tkinter.Label(window, text = 'tictactoe game', font = ('Arial', 50, 'bold'), bg = '#aaaaaa', fg = '#770000')
addtitle.pack()

#adding buttons
buttons = tkinter.Frame(window)
buttons.rowconfigure([1,2,3], pad = 5)
buttons.columnconfigure([1,2,3], pad = 5)
buttons.configure(width = 125, height = 75)

one = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4', command = lambda: press(one))
one.grid(row = 1, column = 1)
two = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(two))
two.grid(row = 1, column = 2)
three = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(three))
three.grid(row = 1, column = 3)

four = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(four))
four.grid(row = 2, column = 1)
five = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(five))
five.grid(row = 2, column = 2)
six = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(six))
six.grid(row = 2, column = 3)

seven = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(seven))
seven.grid(row = 3, column = 1)
eight = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(eight))
eight.grid(row = 3, column = 2)
nine = tkinter.Button(buttons, text = '', font = ('Cambria', 20, 'bold'), width = '8', height = '4',  command = lambda: press(nine))
nine.grid(row = 3, column = 3)
buttons.pack()

score = tkinter.Frame(window)
playerx = tkinter.Label(score, text = 'X', font = ('Cambria', 50, 'bold'), fg = 'white', bg = 'black')
playery = tkinter.Label(score,text = 'O', font = ('Cambria', 50, 'bold'), fg = 'white', bg = 'black')
playerx.place(x = 0, y = 0)
playery.place(x = 2, y = 0)
score.pack()






#functions
counter = 0
check = True
def press(x):
    global counter, check
    if check == True and x['text'] == '':
        x['text'] = 'X'
        x.config(state = 'disabled')
        check = False
        counter += 1
        checkifwon()
    elif check == False and x['text'] == '':
        x['text'] = 'O'
        x.config(state = 'disabled')
        check = True
        counter += 1
        checkifwon()
    

xscore = 0
oscore = 0

#check for wins
def checkifwon():
    global xscore
    global yscore
    if one['text'] == 'X' and two['text'] == 'X' and three['text'] == 'X':
        one.config(bg = 'red', fg = '#ffffff')
        two.config(bg = 'red', fg = '#ffffff')
        three.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        xscore += 1
        clear()
    elif four['text'] == 'X' and five['text'] == 'X' and six['text'] == 'X' :
        four.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        six.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif seven['text'] == 'X' and eight['text'] == 'X' and nine['text'] == 'X' :
        seven.config(bg = 'red', fg = '#ffffff')
        eight.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif one['text'] == 'X' and four['text'] == 'X' and seven['text']== 'X' :
        one.config(bg = 'red', fg = '#ffffff')
        four.config(bg = 'red', fg = '#ffffff')
        seven.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif two['text'] == 'X' and five['text'] == 'X' and eight['text'] == 'X':
        two.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        eight.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif three['text'] == 'X' and six['text'] == 'X' and nine['text'] == 'X':
        three.config(bg = 'red', fg = '#ffffff')
        six.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif one['text'] == 'X' and five['text'] == 'X' and nine['text'] == 'X' :
        one.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
    elif three['text'] == 'X' and five['text'] == 'X' and seven['text'] == 'X':
        three.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        seven.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'X wins')
        clear()
        
    elif one['text'] == 'O' and two['text'] == 'O' and three['text'] == 'O':
        one.config(bg = 'red', fg = '#ffffff')
        two.config(bg = 'red', fg = '#ffffff')
        three.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif four['text'] == 'O' and five['text'] == 'O' and six['text'] == 'O' :
        four.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        six.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif seven['text'] == 'O' and eight['text'] == 'O' and nine['text'] == 'O' :
        seven.config(bg = 'red', fg = '#ffffff')
        eight.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif one['text'] == 'O' and four['text'] == 'O' and seven['text']== 'O' :
        one.config(bg = 'red', fg = '#ffffff')
        four.config(bg = 'red', fg = '#ffffff')
        seven.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif two['text'] == 'O' and five['text'] == 'O' and eight['text'] == 'O':
        two.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        eight.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif three['text'] == 'O' and six['text'] == 'O' and nine['text'] == 'O':
        three.config(bg = 'red', fg = '#ffffff')
        six.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif one['text'] == 'O' and five['text'] == 'O' and nine['text'] == 'O' :
        one.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        nine.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    elif three['text'] == 'O' and five['text'] == 'O' and seven['text'] == 'O':
        three.config(bg = 'red', fg = '#ffffff')
        five.config(bg = 'red', fg = '#ffffff')
        seven.config(bg = 'red', fg = '#ffffff')
        messagebox.showinfo('tic tac toe', 'O wins')
        clear()
    else:
            if counter == 9:
                messagebox.showinfo('tic tac toe' ,"nobody wins, it's a tie")
                clear()
        
def clear():
    global counter
    one.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    two.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    three.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    four.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    five.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    six.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    seven.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    eight.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    nine.config(bg = 'white', fg = 'black', text = '', state = 'normal')
    counter = 0

