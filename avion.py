import dessinMSDA as des
import turtle

des.tl.penup()
des.tl.setpos(-45, -150)
des.tl.setheading(-15)
des.tl.pendown()

# Aile Droite arriere
des.tl.begin_fill()
des.trapeze_Gauche(70, 20, 80, 36.66,'blue', 'blue')
des.tl.end_fill()

# ===================================================================
des.tl.penup()
des.tl.setpos(-30, -55)
des.tl.setheading(-15)
des.tl.pendown()

# Aile Droite avant
des.tl.begin_fill()
des.trapeze_Gauche(105, 30, 120, 55, 'blue', 'blue')
des.tl.end_fill()

# ===================================================================
des.tl.penup()
des.tl.setpos(-30, -150)
des.tl.setheading(-165)
des.tl.pendown()

# Aile Gauche arriere
des.tl.begin_fill()
des.trapeze(70, 20, 80, 36.66,'blue', 'blue')
des.tl.end_fill()

# ===================================================================
des.tl.penup()
des.tl.setpos(-30, -55)
des.tl.setheading(-165)
des.tl.pendown()

# Aile Gauche avant
des.tl.begin_fill()
des.trapeze(105, 30, 120, 55, 'blue', 'blue')
des.tl.end_fill()

# ===================================================================
des.tl.penup()
des.tl.setpos(-42.5, 115)
des.tl.pendown()

# Le long de l'avion
des.tl.begin_fill()
des.rectangle(250, 50, 'blue', 'blue')
des.tl.end_fill()

des.tl.penup()
des.tl.setpos(-42.5, 115)
des.tl.pendown()

# ===================================================================
# Le tete de l'avion
des.tl.begin_fill()
des.cercle(25, 'blue', 'blue')
des.tl.end_fill()

#cest pour masquer la fleche a la fin
des.tl.penup()
des.tl.right(90)
des.tl.pendown()

turtle.done()