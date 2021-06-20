import dessinMSDA as des
import turtle

# CARRE
des.tl.begin_fill()
des.carre(50, 'orange', "orange")
des.tl.end_fill()

# CERCLE 
des.tl.penup()
des.tl.setpos(105, 0)
des.tl.pendown()
des.cercle(50, "green")

# DEMI CERCLE 
des.tl.penup()
des.tl.setpos(160, 0)
des.tl.pendown()
des.demi_cercle(50, "yellow")

# RECTANGLE 
des.tl.penup()
des.tl.setpos(215, 0)
des.tl.pendown()
des.rectangle(50, 30, "black")

# TRIANGLE 
des.tl.penup()
des.tl.setpos(-55, 0)
des.tl.pendown()
des.triangle(50, "blue")

# POLYGONE 
des.tl.penup()
des.tl.setpos(-125, 0)
des.tl.pendown()
des.polygone(8, 50, "green")

# LOSANGE 
des.tl.penup()
des.tl.setpos(-185, 0)
des.tl.pendown()
des.losange(50, "black")

# TRAPEZE 
des.tl.penup()
des.tl.setpos(0, 150)
des.tl.pendown()
des.trapeze(105, 30, 120, 55, 'orange')

turtle.done()