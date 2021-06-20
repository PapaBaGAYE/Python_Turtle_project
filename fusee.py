import turtle
import dessinMSDA as des

# triangle en bas
des.triangle(80, "black")

des.tl.penup()
des.tl.setpos(30, 0)
des.tl.pendown()

# rectangle au milieu
des.rectangle(20, 50, 'black')

des.tl.penup()
des.tl.setpos(30, 50)
des.tl.pendown()

# carree en haut du rectangle
des.tl.begin_fill()
des.carre(20, 'black', "white")
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(20, 55)
des.tl.pendown()

# petit cercle gauche
des.cercle(5,"black")

des.tl.penup()
des.tl.setpos(60, 55)
des.tl.pendown()

# petit cercle droit
des.cercle(5,"black")

des.tl.penup()
des.tl.setpos(5, 70)
des.tl.pendown()

# rectangle en haut du carre et des petits cercles
des.rectangle(70,30, "black")

des.tl.penup()
des.tl.setpos(20, 100)
des.tl.pendown()

#carrre en haut du rectangle
des.carre(40,"black")

des.tl.penup()
des.tl.setpos(5, 105)
des.tl.pendown()

# grand cercle gauche
des.cercle(12.5,"black")

des.tl.penup()
des.tl.setpos(75, 105)
des.tl.pendown()

# grand cercle droit
des.cercle(12.5,"black")

des.tl.penup()
des.tl.setpos(-10, 140)
des.tl.pendown()

# rectangle en haut des grands cercles et du grand carree
des.rectangle(100, 30, 'black')

des.tl.penup()
des.tl.setpos(-40, 140)
des.tl.pendown()

# carre gauche a coté du rectangle
des.carre(30, "black")

des.tl.penup()
des.tl.setpos(90, 140)
des.tl.pendown()

# carre droite a coté du rectangle
des.carre(30, "black")

des.tl.penup()
des.tl.setpos(-10, 170)
des.tl.pendown()

# rectangle en haut des grands cercles et du grand carree
des.rectangle(100, 20, 'black')

des.tl.penup()
des.tl.setpos(-40, 140)
des.tl.pendown()

# triangle a gauche sous les petits carres
des.triangle_Isocele(30,90, "black") 

des.tl.penup()
des.tl.setpos(90, 140)
des.tl.setheading(0)
des.tl.pendown()

# triangle a droit sous petits carres
des.triangle_Isocele(30,90, "black")

des.tl.penup()
des.tl.setpos(-10, 190)
des.tl.setheading(0)
des.tl.pendown()

#triangle en haut du rectangle
des.triangle(100, "black")

des.tl.penup()
des.tl.setpos(16.5, 190)
des.tl.setheading(0)
des.tl.pendown()

#carree a l'interieur du triangle
des.carre(46, "black")

des.tl.penup()
des.tl.setpos(0, 235)
des.tl.pendown()

#triangle en haut du rectangle
des.tl.begin_fill()
des.triangle(80,"black", "white")
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(22, 235)
des.tl.pendown()

#carree a l'interieur du triangle
des.carre(37, "black")

des.tl.penup()
des.tl.setpos(-10, 190)
des.tl.left(-145)
des.tl.pendown()
des.tl.forward(40)

des.tl.penup()
des.tl.setpos(90, 190)
des.tl.right(-110)
des.tl.pendown()
des.tl.forward(40)


turtle.done()