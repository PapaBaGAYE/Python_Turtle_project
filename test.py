import dessinMSDA as des
import turtle

# TEST DU CARRE
des.tl.begin_fill()
des.carre(50, 'orange', "orange")
des.tl.end_fill()

# TEST DU CERCLE 
des.tl.penup()
des.tl.setpos(105, 0)
des.tl.pendown()
des.cercle(50, "green")

# TEST DU DEMI CERCLE 
des.tl.penup()
des.tl.setpos(160, 0)
des.tl.pendown()
des.demi_cercle(50, "yellow")

# TEST DU RECTANGLE 
des.tl.penup()
des.tl.setpos(215, 0)
des.tl.pendown()
des.rectangle(50, 30, "black")

# TEST DU TRIANGLE 
des.tl.penup()
des.tl.setpos(-55, 0)
des.tl.pendown()
des.triangle(50, "blue")

# TEST DU POLYGONE 
des.tl.penup()
des.tl.setpos(-125, 0)
des.tl.pendown()
des.polygone(8, 50, "green")

# TEST DU LOSANGE 
des.tl.penup()
des.tl.setpos(-185, 0)
des.tl.pendown()
des.losange(50, "black")

# TEST DU TRAPEZE 
des.tl.penup()
des.tl.setpos(0, 150)
des.tl.pendown()
des.trapeze(105, 30, 120, 55, 'orange')

turtle.done()