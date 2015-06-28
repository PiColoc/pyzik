#!/usr/bin/python3.4

import geometry, objet

#Constantes physiques
G = 6.67384e-11


def norme_default(objet1, objet2):
	return 0.
class Force:
	def __init__(self, objet1 = objet.Objet(x=1), objet2 = objet.Objet(y=1), norme = norme_default, name = ''):
		self.objet1 = objet1
		self.objet2 = objet2
		self.norme = norme
		self.vecteur = (self.objet2.position - self.objet1.position)
		self.vecteur = self.vecteur * (1/self.vecteur.norme())
		self.vecteur = self.vecteur * self.norme(self.objet1, self.objet2)
		self.name = name
	
	def maj(self):
		self.vecteur = (self.objet2.position - self.objet1.position)
		self.vecteur = self.vecteur * (1/self.vecteur.norme()) 
		self.vecteur = self.vecteur * self.norme(self.objet1, self.objet2) 
	
	def __add__(self, autre_vecteur):
		return self.vecteur + autre_vecteur
	def __str__(self):
		return "objet1: {}\nobjet2: {}\nvecteur: {}\nnom: {}".format(self.objet1, self.objet2, self.vecteur, self.name)

def norme_gravite(objet1, objet2):
	return (objet1.masse * objet2.masse * G /(objet.distance(objet1, objet2)**2))

def maj_force(liste_force):
	for i in range(0,len(liste_force)):
		liste_force[i].maj()

if __name__ == "__main__":
	f = Force(objet.Objet(1.,2.,geometry.Vecteur(1,1),1, "caillou1"), objet.Objet(-1.,2.,geometry.Vecteur(-1,1),1, "caillou2"), norme_gravite, "gravite")
	print(f)
