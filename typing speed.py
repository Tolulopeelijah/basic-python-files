import tkinter, time, random, tkinter.ttk, string
from tkinter import scrolledtext
window = tkinter.Tk()
window.geometry('1366x768')
window.resizable(0,0)
window.overrideredirect(True)

wd = 5 #keyboard width
ht = 1 #keyboard height
wrong, Time, totaltime = 0, 1, 10

def start_timer():
    #area.configure(state  = 'normal')
    global Time, wrong
    
    while Time != totaltime:
        area.focus()
        area.configure(state  = 'normal')
    
    for Time in range(1, totaltime + 1):
        elapsedtime_value.configure(text = Time)
        rmt = totaltime - Time
        remainingtime_value.configure(text = rmt)
        time.sleep(1)
        window.update()

    if Time != totaltime:
        wordlists = area.get(1.0, 'end')
        wordlists = wordlists.split(' ')
            #print(wordlists, '\n')
        totalwords = len(wordlists)

        totalwords_value.configure(text = totalwords)
        sentencelists = sentence.split(' ')
            #print(sentencelists)
    elif Time == totaltime:
        for i, j in zip(wordlists, sentencelists):
            if i != j:
                wrong += 1
        wrongwords_value.configure(text = wrong)
            


        wpmvalue = (totalwords)/totaltime * 60
        wpm_value.configure(text = wpmvalue)
        gross_wpm = totalwords
            #print(totalwords, wrong, gross_wpm)
            
        accuracyvalue = (totalwords - wrong)/totalwords * 100
        accuracy  = round(accuracyvalue) 
        accuracy_value.configure(text = (accuracy, '%'))
        

   
def resetfunction():
    global wrong, Time, totaltime
    wrong, Time, totaltime = 0, 1, 60
    area.configure(text = "", state  = 'disabled')
    wpm_value.configure(text = '')
    wrongwords_value.configure(text = 0)
    accuracy_value.configure(text = (0, '%'))
    remainingtime_value.configure(text = rmt)
    totalwords_value.configure(text = len(sentence.split()))
    elapsedtime_value.configure(text = Time)




######################################################
sentence = "\tCall your mom at least once a week and just tell her \"Mom, I love you\". You don't need a reason for this. Just do it. She will be very happy to receive this call.\n\tCall your dad at least once a week and just say \"Dad, I love you\". Fathers also appreciate positive thoughts from their kids. That will make his day a great one.\n\tFor those of you without parents, call the special people in your life. Who have made difference. Just let them know that you are thinking of them, and that their presence in your life has made a great difference.\n\tSit in silence and appreciate the silence around you. Ask the universe to grant other that same great feeling of peace, security and tranquility.\n Feed the ducks or birds at your·local park. We get caught up in our day to day activities and forget the simple joy of something like feeding the birds. Birds always enjoy a fresh piece of bread."
#############################################################
title = tkinter.Frame(window)
name = tkinter.Label(title, text = 'TYPING TEST', font = ('algerian', 30, 'bold'), width = 53, bg = '#4499ff', fg = 'black')
name.grid()
title.grid(row = 1, column = 0)

#####################################################
texts = tkinter.Frame(window)
words = tkinter.Label(texts, text = sentence, font = ('Comic sans ms', 12), fg = 'black', wraplength = 1000, justify = 'left')
words.grid()
texts.grid(row = 2, column = 0)
######################################################
textarea = tkinter.Frame(window)
area = tkinter.Text(textarea, font = ('Cambria', 14, 'bold'), width = 87, height = 8, bd = 4, relief = 'groove', wrap = 'word', state = 'disabled')
area.grid()
textarea.grid(row = 3, column = 0)

#######################################################
output = tkinter.Frame(window)
elapsedtime = tkinter.Label(output, text = 'Elapsed Time: ', font = ('Arial', 12, 'bold'), fg = 'red')
elapsedtime.grid()

elapsedtime_value = tkinter.Label(output, text = '0', font = ('Arial', 12, 'bold'))
elapsedtime_value.grid(row = 0, column = 1, padx = 5)

remainingtime = tkinter.Label(output, text = 'Remaining Time: ', font = ('Arial', 12, 'bold'), fg = 'red')
remainingtime.grid(row = 0, column = 2, padx = 5)

remainingtime_value = tkinter.Label(output, text = '60', font = ('Arial', 12, 'bold'))
remainingtime_value.grid(row = 0, column = 3, padx = 5)

wpm = tkinter.Label(output, text = 'WPM: ', font = ('Arial', 12, 'bold'), fg = 'red')
wpm.grid(row = 0, column = 4, padx = 5)

wpm_value = tkinter.Label(output, text = '0', font = ('Arial', 12, 'bold'))
wpm_value.grid(row = 0, column = 5, padx = 5)

accuracy = tkinter.Label(output, text = 'Accuracy: ', font = ('Arial', 12, 'bold'), fg = 'red')
accuracy.grid(row = 0, column = 6, padx = 5)

accuracy_value = tkinter.Label(output, text = '0', font = ('Arial', 12, 'bold'))
accuracy_value.grid(row = 0, column = 7, padx = 5)

totalwords = tkinter.Label(output, text = 'Total Words: ', font = ('Arial', 12, 'bold'), fg = 'red')
totalwords.grid(row = 0, column = 8, padx = 5)

totalwords_value = tkinter.Label(output, text = '0', font = ('Arial', 12, 'bold'))
totalwords_value.grid(row = 0, column = 9, padx = 5)

wrongwords = tkinter.Label(output, text = 'Wrong Words: ', font = ('Arial', 12, 'bold'), fg = 'red')
wrongwords.grid(row = 0, column = 10, padx = 5)

wrongwords_value = tkinter.Label(output, text = '0', font = ('Arial', 12, 'bold'))
wrongwords_value.grid(row = 0, column = 11, padx = 5)

output.grid(row = 4, column = 0)

################################################################
buttons = tkinter.Frame(window)

start = tkinter.Button(buttons, text = 'Start', width = 12, font = ('arial', 10, 'bold'), fg = 'white', bg = '#ff4400', command = start_timer)
start.grid(row  = 0, column = 0, padx = 10)

reset = tkinter.Button(buttons, text = 'Reset', width = 12, font = ('arial', 10, 'bold'), fg = 'white', bg = '#999900', state = 'disabled', command = resetfunction)
reset.grid(row  = 0, column = 1, padx = 10)

exitbutton = tkinter.Button(buttons, text = 'Exit', width = 12, font = ('arial', 10, 'bold'), fg = 'white', bg = '#ff4400', command = exit)
exitbutton.grid(row  = 0, column = 2, padx = 10)

buttons.grid(row = 5, column = 0, pady = 15)

####################################################################
keyboards = tkinter.Frame(window)

numbers = tkinter.Frame(keyboards)

appr = tkinter.Label(numbers, text = '~\n `', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
appr.grid(row = 0, column = 0)
one = tkinter.Label(numbers, text = '!\n1', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
one.grid(row = 0, column = 1,padx = 2, pady = 2)

two = tkinter.Label(numbers, text = '@\n2', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
two.grid(row = 0, column = 2,padx = 2, pady = 2)

three = tkinter.Label(numbers, text = '#\n3', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
three.grid(row = 0, column = 3,padx = 2, pady = 2)

four = tkinter.Label(numbers, text = '$\n4', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
four.grid(row = 0, column = 4,padx = 2, pady = 2)

five = tkinter.Label(numbers, text = '%\n5', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
five.grid(row = 0, column = 5,padx = 2, pady = 2)

six = tkinter.Label(numbers, text = '^\n6', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
six.grid(row = 0, column = 6,padx = 2, pady = 2)

seven = tkinter.Label(numbers, text = '&\n7', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
seven.grid(row = 0, column = 7,padx = 2, pady = 2)

eight = tkinter.Label(numbers, text = '*\n8', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
eight.grid(row = 0, column = 8,padx = 2, pady = 2)

nine = tkinter.Label(numbers, text = '(\n9', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
nine.grid(row = 0, column = 9,padx = 2, pady = 2)

zero = tkinter.Label(numbers, text = ')\n0', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
zero.grid(row = 0, column = 10,padx = 2, pady = 2)

minus = tkinter.Label(numbers, text = '-\n _', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
minus.grid(row = 0, column = 11,padx = 2, pady = 2)

plus = tkinter.Label(numbers, text = '+\n=', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
plus.grid(row = 0, column = 12,padx = 2, pady = 2)

backspace = tkinter.Label(numbers, text = 'Back\nSpace', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 10, height = 2, relief = 'raised', bd = 5)
backspace.grid(row = 0, column = 13, padx = 4, pady = 2)
numbers.grid(row = 0, column = 0)

qwe = tkinter.Frame(keyboards)
#               SECOND LINE

tab = tkinter.Label(qwe, text = 'Tab ---->', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 7, height = ht, relief = 'raised', bd = 5)
tab.grid(row = 0, column = 0, padx = 3, pady = 2)

q = tkinter.Label(qwe, text = 'Q', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
q.grid(row = 0, column = 1, padx = 3, pady = 2)

w = tkinter.Label(qwe, text = 'W', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
w.grid(row = 0, column = 2, padx = 3, pady = 2)

e = tkinter.Label(qwe, text = 'E', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
e.grid(row = 0, column = 3, padx = 3, pady = 2)

r = tkinter.Label(qwe, text = 'R', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
r.grid(row = 0, column = 4, padx = 3, pady = 2)

t = tkinter.Label(qwe, text = 'T', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
t.grid(row = 0, column = 5, padx = 3, pady = 2)

y = tkinter.Label(qwe, text = 'Y', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
y.grid(row = 0, column = 6, padx = 3, pady = 2)

u = tkinter.Label(qwe, text = 'U', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
u.grid(row = 0, column = 7, padx = 3, pady = 2)

i = tkinter.Label(qwe, text = 'I', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
i.grid(row = 0, column = 8, padx = 3, pady = 2)

o = tkinter.Label(qwe, text = 'O', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
o.grid(row = 0, column = 9, padx = 3, pady = 2)

p = tkinter.Label(qwe, text = 'P', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
p.grid(row = 0, column = 10, padx = 3, pady = 2)

square = tkinter.Label(qwe, text = '{\n[', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
square.grid(row = 0, column = 11, padx = 2, pady = 2)

closed = tkinter.Label(qwe, text = '}\n]', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = wd, height = ht, relief = 'raised', bd = 5)
closed.grid(row = 0, column = 12, padx = 3, pady = 2)

Enter = tkinter.Label(qwe, text = 'Enter', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 6, height = ht, relief = 'raised', bd = 5)
Enter.grid(row = 0, column = 13, padx = 2, pady = 2)


qwe.grid(row = 1, column = 0)

#       THIRD LINE
asd =  tkinter.Frame(keyboards)

caps = tkinter.Label(asd, text = 'CAPS\nLOCK', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 11, height = 2, relief = 'raised', bd = 5)
caps.grid(row = 0, column = 0, padx = 5, pady = 2)

a = tkinter.Label(asd, text = 'A', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
a.grid(row = 0, column = 1, padx = 4, pady = 2)

s = tkinter.Label(asd, text = 'S', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
s.grid(row = 0, column = 2, padx = 4, pady = 2)

d = tkinter.Label(asd, text = 'D', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
d.grid(row = 0, column = 3, padx = 4, pady = 2)

f = tkinter.Label(asd, text = 'F\n      _', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
f.grid(row = 0, column = 4, padx = 4, pady = 2)

g = tkinter.Label(asd, text = 'G', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
g.grid(row = 0, column = 5, padx = 4, pady = 2)

h = tkinter.Label(asd, text = 'H', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
h.grid(row = 0, column = 6, padx = 4, pady = 2)

j = tkinter.Label(asd, text = 'J\n_', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
j.grid(row = 0, column = 7, padx = 4, pady = 2)

k = tkinter.Label(asd, text = 'K', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
k.grid(row = 0, column = 8, padx = 4, pady = 2)

l = tkinter.Label(asd, text = 'L', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
l.grid(row = 0, column = 9, padx = 4, pady = 2)

colon = tkinter.Label(asd, text = ':\n;', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
colon.grid(row = 0, column = 10, padx = 4, pady = 2)

at = tkinter.Label(asd, text = '"\n\'', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
at.grid(row = 0, column = 11, padx = 4, pady = 2)

Enter = tkinter.Label(asd, text = '<--\'', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 4, height = 2, relief = 'raised', bd = 5)
Enter.grid(row = 0, column = 13, padx = 13, pady = 2)


asd.grid(row = 2, column = 0)

#               FOURTH LINE
zxc = tkinter.Frame(keyboards)
shift1 = tkinter.Label(zxc, text = 'SHIFT', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 6, height = 2, relief = 'raised', bd = 5)
shift1.grid(row = 0, column = 0, padx = 3, pady = 2)

bwdslsh = tkinter.Label(zxc, text = '|\n\\', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
bwdslsh.grid(row = 0, column = 1, padx = 3, pady = 2)

z = tkinter.Label(zxc, text = 'Z', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
z.grid(row = 0, column = 2, padx = 3, pady = 2)

x = tkinter.Label(zxc, text = 'X', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
x.grid(row = 0, column = 3, padx = 3, pady = 2)

c = tkinter.Label(zxc, text = 'C', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
c.grid(row = 0, column = 4, padx = 3, pady = 2)

v = tkinter.Label(zxc, text = 'V', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
v.grid(row = 0, column = 5, padx = 3, pady = 2)

b = tkinter.Label(zxc, text = 'B', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
b.grid(row = 0, column = 6, padx = 3, pady = 2)

n = tkinter.Label(zxc, text = 'N', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
n.grid(row = 0, column = 7, padx = 3, pady = 2)

m = tkinter.Label(zxc, text = 'M', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
m.grid(row = 0, column = 8, padx = 3, pady = 2)

lt = tkinter.Label(zxc, text = '<\n,', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
lt.grid(row = 0, column = 9, padx = 3, pady = 2)

gt = tkinter.Label(zxc, text = '>\n.', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
gt.grid(row = 0, column = 10, padx = 3, pady = 2)

fwdslsh = tkinter.Label(zxc, text = '?\n/', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 5, height = 2, relief = 'raised', bd = 5)
fwdslsh.grid(row = 0, column = 11, padx = 3, pady = 2)

shift2 = tkinter.Label(zxc, text = 'SHIFT', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 13, height = 2, relief = 'raised', bd = 5)
shift2.grid(row = 0, column = 12, padx = 5, pady = 2)

zxc.grid(row = 3, column = 0)

#       FIFTH LINE
spaces = tkinter.Frame(keyboards)
space = tkinter.Label(spaces, text = '', bg = 'black', fg = 'white', font = ('arial', 12, 'bold'), width = 30, height = 2, relief = 'raised', bd = 5)
space.grid(row = 1, column = 5)
spaces.grid(row = 4, column =0)


keyboards.grid(row = 6, column = 0)
####################################################################################
############### FUNCTIONS###############
numbers = [one,two,three,four,five,six,seven,eight,nine,zero]
letters = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, lt, gt, fwdslsh, bwdslsh, square, closed, at, colon, plus, minus,appr]
alphabets = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
functions = [shift1, shift2, caps, tab, Enter]
spacebar = [space]


bindnums = [1,2,3,4,5,6,7,8,9,0]
bindletters = list(string.ascii_lowercase) + [',', '.', '/', '\\', '[', ']', '\'', ';', '=', '-','`']
fullcaps = list(string.ascii_uppercase)+ [',', '.', '/', '\\', '[', ']', '\'', ';', '=', '-','`']
bindletterscaps = list(string.ascii_uppercase)

def Changecolor(widget, case, default):
    
    widget.configure(bg = 'blue',text = case)
    widget.after(100, lambda: widget.configure(bg = 'black', text = default))
    
def changecolor(widget):
    
    widget.configure(bg = 'blue')
    widget.after(100, lambda: widget.configure(bg = 'black'))

for num, _ in enumerate(bindnums):
    window.bind(bindnums[num], lambda event, lbl = numbers[num]: changecolor(lbl))

for let, _ in enumerate(bindletters):
    window.bind(bindletters[let], lambda event, lbl = letters[let], case = bindletters[let], default = fullcaps[let]: Changecolor(lbl, case, default))

for LET, _ in enumerate(bindletterscaps):
    window.bind(bindletterscaps[LET], lambda event, lbl = alphabets[LET]: changecolor(lbl))

window.bind('<space>', lambda event: changecolor(space))
for i, j in enumerate(bindletterscaps):
    window.bind('<Shift-{}>'.format(j), lambda event: changecolor(shift1))




