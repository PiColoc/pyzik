#! /usr/bin/python3.4

import geometry, objet, force, objet

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

for i in range(0,len(liste_objet)):
	for j in range(0, len(liste_force)):
		for k in range(0, len(liste_objet)):
			if i != k:
				liste_objet[i].add_force(liste_force[j])
				liste_objet[i].forces[len(liste_objet[i].forces)-1].objet1 = liste_objet[i]
				liste_objet[i].forces[len(liste_objet[i].forces)-1].objet2 = liste_objet[k]


def clavier(event):
	for i in range(0,len(liste_objet)):
		force.maj_force(liste_objet[i].forces)
	for i in range(0,len(liste_objet)):
		liste_objet[i].tic()
	canvas.coords(objet1_i, 250+liste_objet[0].position.x/zoom,250+liste_objet[0].position.y/zoom,250+liste_objet[0].position.x/zoom+25,250+liste_objet[0].position.y/zoom+25)
	canvas.coords(objet2_i,250+ liste_objet[1].position.x/zoom, 250+liste_objet[1].position.y/zoom,250+liste_objet[1].position.x/zoom+10,250+liste_objet[1].position.y/zoom+10)
	canvas.coords(objet3_i,250+ liste_objet[2].position.x/zoom, 250+liste_objet[2].position.y/zoom,250+liste_objet[2].position.x/zoom+50,250+liste_objet[2].position.y/zoom+50)



from tkinter import *


fenetre = Tk()
canvas = Canvas(fenetre,width = 1250, height = 650, background = 'white')
objet1_i = canvas.create_oval(liste_objet[0].position.x,liste_objet[0].position.y,liste_objet[0].position.x+50,liste_objet[0].position.y+50, fill = 'black')
objet2_i = canvas.create_oval(liste_objet[1].position.x,liste_objet[1].position.y,liste_objet[1].position.x+50,liste_objet[1].position.y+50, fill = 'green')
objet3_i = canvas.create_oval(liste_objet[1].position.x,liste_objet[1].position.y,liste_objet[1].position.x+50,liste_objet[1].position.y+50, fill = 'yellow')
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()
fenetre.mainloop()



