#! /usr/bin/python3.4

import math

class Vecteur:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def norme(self):
		return math.sqrt(self.x**2 + self.y**2)
	
	def __add__(self, autre_vecteur):
		v = Vecteur(self.x + autre_vecteur.x, self.y + autre_vecteur.y)
		return v

	def __mul__(self, l):
		return Vecteur(l * self.x, l * self.y)

	def __sub__(self, autre_vecteur):
		return self + autre_vecteur * (-1)
	
	def __repr__(self):
		return "vecteur:x({}), y({})".format(self.x, self.y) 
	def __str__(self):
		return "({},{})".format(self.x, self.y)

if __name__ == "__main__":
	v = Vecteur()
	v = v * 1.0
	print(v)
