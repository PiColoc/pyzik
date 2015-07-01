#! /usr/bin/python3.4

import geometry, objet, force, objet
from tkinter import *

zoom = 1000000000
pas = 3600*24

liste_objet = []
liste_force = []

# Ajout des forces

liste_force.append(force.Force(norme = force.norme_gravite, name = 'gravite')) # On ajoute la gravite

# Ajout des objets
def ajout_objet(x,y,v,masse,nom):
	liste_objet.append(objet.Objet(x,y,v,masse,nom))

ajout_objet(0,0,geometry.Vecteur(), 5.972e24, 'terre')
ajout_objet(0.0,384400000,geometry.Vecteur(0,0),7.3477e22, 'lune') #1000
ajout_objet(0.0,150e9,geometry.Vecteur(0,0), 2e30, 'soleil')

# Prétraitement des objets

for obj in liste_objet:
	for force in liste_force:
		for obj2 in liste_objet:
			if obj != obj2:
				obj.add_force(force)
				obj.forces[len(obj.forces)-1].objet1 = obj
				obj.forces[len(obj.forces)-1].objet2 = obj2


def clavier(event):
	for obj in liste_objet:
		force.maj_force(obj.forces)
	for obj in liste_objet:
		obj.tic()

    obj0,obj1,obj2 = liste_objet[0:2]
	
    canvas.coords(objet1_i, 
                250 + obj0.position.x/zoom,
                250 + obj0.position.y/zoom,
                250 + obj0.position.x/zoom + 25,
                250 + obj0.position.y/zoom + 25)

	canvas.coords(objet2_i,
                250 + obj1.position.x/zoom, 
                250 + obj1.position.y/zoom,
                250 + obj1.position.x/zoom + 10,
                250 + obj1.position.y/zoom + 10)

	canvas.coords(objet3_i,
                250 + obj2.position.x/zoom, 
                250 + obj2.position.y/zoom, 
                250 + obj2.position.x/zoom + 50,
                250 + obj2.position.y/zoom + 50)


fenetre = Tk()
canvas = Canvas(fenetre,width = 1250, height = 650, background = 'white')

obj0,obj1,obj2 = liste_objet[0:2]

objet1_i = canvas.create_oval(obj0.position.x,
                             obj0.position.y,
                             obj0.position.x+50,
                             obj0.position.y+50, 
                             fill = 'black')

objet2_i = canvas.create_oval(obj1.position.x,
                             obj1.position.y,
                             obj1.position.x + 50,
                             obj1.position.y + 50, 
                             fill = 'green')

objet3_i = canvas.create_oval(obj1.position.x,
                             obj1.position.y,
                             obj1.position.x + 50,
                             obj1.position.y + 50, 
                             fill = 'yellow')

canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()
fenetre.mainloop()



