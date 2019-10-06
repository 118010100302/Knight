from turtle import *
setup(600,400,None,None)
bgcolor("red")
fillcolor("yellow")
pencolor("yellow")
speed(8)
#主星
begin_fill()
penup()
goto(-260,100)
pendown()
for i in range(5):
 fd(120)
 right(144)
end_fill()
#第一颗副星
begin_fill()
penup()
goto(-115,175)
seth(-30)
pendown()
for i in range(5):
 fd(40)
 right(144)
end_fill()
#第二颗副星
begin_fill()
penup()
goto(-70,135)
seth(-35)
pendown()
for i in range(5):
 fd(40)
 right(144)
end_fill()
#第三颗副星
begin_fill()
penup()
goto(-80,70)
seth(0)
pendown()
for i in range(5):
 fd(40)
 right(144)
end_fill()
#第四颗副星
begin_fill()
penup()
goto(-115,35)
seth(-30)
pendown()
for i in range(5):
 fd(40)
 right(144)
end_fill()
