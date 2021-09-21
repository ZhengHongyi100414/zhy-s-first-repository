import turtle
import datetime
import time
t=turtle.Turtle()
t.speed(0)
def board(r):#绘制表盘
    t.penup()
    t.setheading(270)
    t.fd(r)
    t.setheading(0)
    t.pendown()
    t.circle(r)
    t.penup()
    t.home()
    t.pendown()
    t.dot()
def num(r):#写数字，打点
    board(r)
    t.setheading(60)
    for i in range(12):
        t.penup()
        t.fd(r)
        t.pendown()
        t.write(i+1)
        t.dot()
        t.penup()
        t.backward(r)
        t.right(30)
        t.hideturtle()
def hms(r):#画针
    h=turtle.Turtle()
    m=turtle.Turtle()
    s=turtle.Turtle()
    h.speed(-2)
    m.speed(-2)
    s.speed(-2)
    while True:            
        ti=datetime.datetime.now()
        angles=[]
        h.pendown()
        m.pendown()
        s.pendown()
        hmsGUI=[h,m,s]
        h_angle = -ti.hour*30-ti.minute*(30/60)-ti.second*(30/60/60)+90
        m_angle=-ti.minute*6-ti.second*(6/60)+90
        s_angle=-ti.second*6+90
        angles=[h_angle,m_angle,s_angle]
        for i in range(3):
            hmsGUI[i].pensize(7-2*(i+1))
            hmsGUI[i].setheading(angles[i])
            hmsGUI[i].fd(((i+1)*0.3)*r)
        turtle.tracer(1) 
        time.sleep(1)
        turtle.tracer(0)

        h.clear()
        m.clear()
        s.clear()
        h.penup()
        m.penup()
        s.penup()
        h.home()
        m.home()
        s.home()
num(200)     
hms(200)
