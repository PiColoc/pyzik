#!/usr/bin/python3.4
# -*-coding:Latin-1 -*

pas = 3600*24

import geometry

class Objet:

	def __init__(self, x = 0, y = 0, v = geometry.Vecteur(), masse = 0, nom = ''):

		self.position = geometry.Vecteur(x, y)
		self.masse = masse
		self.forces = []
		self.position_p = geometry.Vecteur(x, y) - (v * pas)
		self.nom = nom
	
	def tic(self):
		"""met à jour le vecteur position en fonction des forces exercées sur l'objet"""
		temp = self.position
		acceleration = geometry.Vecteur()

		for force in self.forces:
			acceleration += force 

		acceleration *= (1 / self.masse)
		self.position = (self.position * 2) - self.position_p + (acceleration * (pas**2))
		self.position_p = temp
		
	def add_force(self,force):
		self.forces.append(force)

	def __str__(self):
		return "objet(position:{}, masse:{}, position precedente:{}, nom:{})".format(self.position, 
                                                                                    self.masse, 
                                                                                    self.position_p, 
                                                                                    self.nom)

def distance(objet1, objet2):
	return (objet1.position - objet2.position).norme()

if __name__ == "__main__":
	o = Objet(1., 2., geometry.Vecteur(1, 1), 1, "caillou")
	o.add_force(geometry.Vecteur(1., 3.))
	o.tic()
	print(o)
