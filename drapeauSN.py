import dessinMSDA as des
import turtle

# Partie VERTE
des.tl.begin_fill()
des.rectangle(50, 120, "black", "green")
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(50, 0)
des.tl.pendown()

# Partie JAUNE
des.tl.begin_fill()
des.rectangle(50, 120, "black", "yellow")
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(100, 0)
des.tl.pendown()

# Partie ROUGE
des.tl.begin_fill()
des.rectangle(50, 120, "black", "red")
des.tl.end_fill()

des.tl.penup()
des.tl.setheading(45)
des.tl.setpos(70, 50)
des.tl.pendown()

#ETOILE
des.tl.begin_fill()
des.tl.color('green')
angle = 180/5
for i in range(5):
    des.tl.forward(25)
    des.tl.right(angle-180)
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(20, 50)
des.tl.pendown()

turtle.done()