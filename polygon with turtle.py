import turtle
s = turtle.getscreen()
t = turtle.Turtle()
def draw_pentagon():
    a = int(input("how many sides? : "))
    for p in range(a):
        t.rt(360/a)
        t.fd(90)
t.color('red')
draw_pentagon()
