from tkinter import *
from typing import Counter 
from widget_winfo import widget_w, widget_h

w = 500
h = 500
color = '#121212'
mcounter = 1

sc = Tk()
sc.geometry(f'{w}x{h}')
sc.resizable(False, False)
sc.configure(bg=f'{color}')


c = Canvas(width = 400, height = 400, bg=f'{color}')
c.place(x = 50, y = 50)

c.create_line(133,0,133,400, width=7, fill='white')
c.create_line(266,0,266,400, width=7, fill='white')
c.create_line(0,133,400,133, width=7, fill='white')
c.create_line(0,266,400,266, width=7, fill='white')


def game1():
    global mcounter

    if mcounter%2 == 0:
        b1['text'] = 'x'
        b1['disabledforeground'] = 'red'
    else:
        b1['text'] = '0'
        b1['disabledforeground'] = 'green'

    mcounter += 1

    b1['state'] = 'disabled'

    maingame()

def game2():
    global mcounter

    if mcounter%2 == 0:
        b2['text'] = 'x'
        b2['disabledforeground'] = 'red'
    else:
        b2['text'] = '0'
        b2['disabledforeground'] = 'green'

    mcounter += 1

    b2['state'] = 'disabled'

    maingame()

def game3():
    global mcounter

    if mcounter%2 == 0:
        b3['text'] = 'x'
        b3['disabledforeground'] = 'red'
    else:
        b3['text'] = '0'
        b3['disabledforeground'] = 'green'
    mcounter += 1

    b3['state'] = 'disabled'

    maingame()

def game4():
    global mcounter

    if mcounter%2 == 0:
        b4['text'] = 'x'
        b4['disabledforeground'] = 'red'
    else:
        b4['text'] = '0'
        b4['disabledforeground'] = 'green'

    mcounter += 1

    b4['state'] = 'disabled'

    maingame()

def game5():
    global mcounter

    if mcounter%2 == 0:
        b5['text'] = 'x'
        b5['disabledforeground'] = 'red'
    else:
        b5['text'] = '0'
        b5['disabledforeground'] = 'green'

    mcounter += 1

    b5['state'] = 'disabled'

    maingame()

def game6():
    global mcounter

    if mcounter%2 == 0:
        b6['text'] = 'x'
        b6['disabledforeground'] = 'red'
    else:
        b6['text'] = '0'
        b6['disabledforeground'] = 'green'

    mcounter += 1

    b6['state'] = 'disabled'

    maingame()

def game7():
    global mcounter

    if mcounter%2 == 0:
        b7['text'] = 'x'
        b7['disabledforeground'] = 'red'
    else:
        b7['text'] = '0'
        b7['disabledforeground'] = 'green'

    mcounter += 1

    b7['state'] = 'disabled'

    maingame()

def game8():
    global mcounter

    if mcounter%2 == 0:
        b8['text'] = 'x'
        b8['disabledforeground'] = 'red'
    else:
        b8['text'] = '0'
        b8['disabledforeground'] = 'green'

    mcounter += 1

    b8['state'] = 'disabled'

    maingame()

def game9():
    global mcounter

    if mcounter%2 == 0:
        b9['text'] = 'x'
        b9['disabledforeground'] = 'red'
    else:
        b9['text'] = '0'
        b9['disabledforeground'] = 'green'
    
    b9['state'] = 'disabled'
    

    mcounter += 1

    maingame()

    

def maingame():
    if b1['text'] != '':
        if b1['text'] == b2['text']:
            if b2['text'] == b3['text']:
                screen()

    if b4['text'] != '':
        if b4['text'] == b5['text']:
            if b5['text'] == b6['text']:
                screen()

    if b7['text'] != '':
        if b7['text'] == b8['text']:
            if b8['text'] == b9['text']:
                screen()

    if b1['text'] != '':
        if b1['text'] == b4['text']:
            if b4['text'] == b7['text']:
                screen()
    
    if b2['text'] != '':
        if b2['text'] == b5['text']:
            if b5['text'] == b8['text']:
                screen()

    if b3['text'] != '':
        if b3['text'] == b6['text']:
            if b6['text'] == b9['text']:
                screen()
    
    if b1['text'] != '':
        if b1['text'] == b5['text']:
            if b5['text'] == b9['text']:
                screen()

    if b3['text'] != '':
        if b3['text'] == b5['text']:
            if b5['text'] == b7['text']:
                screen()

    



def screen():
    for widget in widgets:
        widget.place_forget()

    win_label = Label(
        text = 'x/0 wins!', bg = '#9966cc',
        fg = 'white', font = ('Icon', 35)
    )
    
    win_label.pack()


b1 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game1
)

b2 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game2
)

b3 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game3
)

b4 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game4
)

b5 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game5
)

b6 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game6
)

b7 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game7
)

b8 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game8
)

b9 = Button(
    bg = f'{color}', font=('Arial Black', 25),
    width = 5, height=2, relief = 'flat',  command = game9
)


bttns = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

b_w = widget_w(b1)
b_h = widget_h(b2)



i = 53
j = 52
counter = 0
for bttn in bttns:
    bttn.place(x = i, y = j)

    counter += 1
    if counter <= 2:
        i += b_w+ 10
    else:
        i = 53
        counter = 0
        j += b_h + 8
    
    


    
widgets = bttns.copy()

widgets.append(c)
sc.mainloop()