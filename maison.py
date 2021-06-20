import turtle 
import dessinMSDA as des

# Dessin du rectangle en fond noir du bas
des.tl.begin_fill()
des.rectangle(100, 20, 'black')
des.tl.end_fill()

# Dessin du rectangle en fond noir du bas
des.carre(100, 'black')

# Dessin du triangle et son deplacement en haut pour le toit
des.tl.penup()
des.tl.setpos(-20, 100)
des.tl.pendown()
des.triangle(140, "black")

# Dessin des petits carrées et leurs deplacement en haut pour la fenetre
deplacement = 60
for i in range(2):
    des.tl.penup()
    des.tl.setpos(75, deplacement)
    des.tl.pendown()
    des.carre(20, "black")

    des.tl.penup()
    des.tl.setpos(55, deplacement)
    des.tl.pendown()
    des.carre(20, "black")
    deplacement-=20

# Dessin du rectangle et son deplacement pour la porte
des.tl.penup()
des.tl.setpos(10, 0)
des.tl.pendown()
des.rectangle(40, 80, "black")

# Dessin du rectangle en fond noir du bas
des.tl.penup()
des.tl.setpos(5, 1)
des.tl.pendown()
des.tl.begin_fill()
des.rectangle(50, 18, 'white', "white")
des.tl.end_fill()

# Dessin du rectangle pour le toit
des.tl.penup()
des.tl.setpos(75, 150)
des.tl.pendown()
des.tl.begin_fill()
des.rectangle(20, 40, 'black', 'white')
des.tl.end_fill()

turtle.done()