import turtle

tl = turtle.Turtle()
#CERCLE
def cercle(rayon,
           couleur,
           couleur2='black'):
    """
    Commentaires de spécification
    Bloc cercle
    Objectif : Ce bloc permet de dessiner un cercle
    Méthode : On dessine un cercle avec le module turtle
    Besoins : rayon, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : cercle
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    tl.circle(rayon)

#DEMI-CERCLE
def demi_cercle(rayon,
                couleur,
                couleur2='black'):
    """
    Commentaires de spécification
    Bloc demi_cercle
    Objectif : Ce bloc permet de dessiner un demi_cercle
    Méthode : On dessine un demi_cercle avec le module turtle
    Besoins : rayon, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : demi_cercle
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    tl.circle(rayon, 180)
    tl.penup()
    tl.circle(rayon, 180)
    tl.pendown()

#CARRE
def carre(cote,
          couleur,
          couleur2='black'):
    """
    Commentaires de spécification
    Bloc carre
    Objectif : Ce bloc permet de dessiner un carre
    Méthode : On dessine un carre avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : carre
    Hypothèses : -
    """
    for i in range(4):
        tl.color(couleur, couleur2)
        tl.forward(cote)
        tl.left(90)

#TRIANGLE
def triangle(cote,
             couleur,
             couleur2='black'):
    """
    Commentaires de spécification
    Bloc triangle
    Objectif : Ce bloc permet de dessiner un triangle
    Méthode : On dessine un triangle avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : triangle
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    for i in range(3):
        tl.forward(cote)
        tl.right(-120)

#TRIANGLE ISOCELE
def triangle_Isocele(cote,
                     cote2,
                     couleur,
                     couleur2='black'):
    """
    Commentaires de spécification
    Bloc triangle
    Objectif : Ce bloc permet de dessiner un triangle
    Méthode : On dessine un triangle avec le module turtle
    Besoins : cote, cote2(les cotés 2 isocèles), couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : triangle isocèle
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    tl.forward(cote)
    tl.left(-100)
    tl.forward(cote2)
    tl.left(-160)
    tl.forward(cote2)

# triangleIsocele(20, 60, 'black')

#RECTANGLE
def rectangle(longueur,
              largeur,
              couleur,
              couleur2='black'):
    """
    Commentaires de spécification
    Bloc rectangle
    Objectif : Ce bloc permet de dessiner un rectangle
    Méthode : On dessine un rectangle avec le module turtle
    Besoins : longueur, largeur, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : rectangle
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    for i in range(2):
        tl.forward(longueur)
        tl.left(90)
        tl.forward(largeur)
        tl.left(90)

# POLYGONE 
def polygone(n,
             cote, 
             couleur, 
             couleur2='black'):
    """
    Commentaires de spécification
    Bloc polygone
    Objectif : Ce bloc permet de dessiner un polygone
    Méthode : On dessine un polygone avec le module turtle a n coté
    Besoins : n, cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : polygone
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    angle = 360.0/n
    for k in range(n):
        tl.forward(cote)
        tl.left(angle)

#LOSANGE
def losange(cote,
            couleur,
            couleur2='black'):
    """
    Commentaires de spécification
    Bloc losange
    Objectif : Ce bloc permet de dessiner un losange
    Méthode : On dessine un losange avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : losange
    Hypothèses : -
    """
    tl.color(couleur,couleur2)   
    for i in range(2):
        tl.forward(cote)
        tl.right(-135)
        tl.forward(cote)
        tl.right(-45)

# ELIPSE
def elipse(cote,
           couleur, 
           couleur2='black'):    
    """
    Commentaires de spécification
    Bloc elipse
    Objectif : Ce bloc permet de dessiner un elipse
    Méthode : On dessine un elipse avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : elipse
    Hypothèses : -
    """
    tl.left(45)
    tl.color(couleur, couleur2)
    for i in range(2):
        tl.circle(cote, 90)
        tl.circle(cote/2, 90)
    tl.left(-45)

#TRAPEZE
def trapeze(cote1,
            cote2,
            cote3,
            cote4,
            couleur,
            couleur2='black'):
    """
    Commentaires de spécification
    Bloc trapeze
    Objectif : Ce bloc permet de dessiner un trapeze
    Méthode : On dessine un trapeze avec le module turtle
    Besoins : cote, couleur et couleur2 (la couleur 2 c'est pour une éventuelle couleur de fond)
    Connues : -
    Entrées : -
    Sorties : -
    Résultats : trapeze
    Hypothèses : -
    """
    tl.color(couleur, couleur2)
    angle1 = 100
    angle2 = 70
    angle3 = 120
    angle4 = 70


    tl.forward(cote1)
    tl.right(angle1)
    tl.forward(cote2)
    tl.right(angle2)
    tl.forward(cote3)
    tl.right(angle3)
    tl.forward(cote4)

def trapeze_Gauche(cote1,
                   cote2,
                   cote3, 
                   cote4, 
                   couleur, 
                   couleur2='black'):
    tl.color(couleur, couleur2)
    angle1 = 100
    angle2 = 70
    angle3 = 120
    angle4 = 70


    tl.forward(cote1)
    tl.left(angle1)
    tl.forward(cote2)
    tl.left(angle2)
    tl.forward(cote3)
    tl.left(angle3)
    tl.forward(cote4)




