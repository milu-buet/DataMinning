# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 4


import math

#-----------------------------------------------------------
class Point:
	Columns = []

	@classmethod
	def set_features(cls, *columns):
		Point.Columns = columns
	

	def __init__(self, row):
		self.row = row
		self.id = None



	def RMS(self, y):
		A = 0
		B = 0
		C = 0
		for c in Point.Columns:
			#s += (self.row[c] - y.row[c])**2
			A += self.row[c]*y.row[c]
			B += self.row[c]**2
			C += y.row[c]**2


		if A == 0:
			A = 1   #Assuming no-active user is similar to no-active user 

		if B == 0:
			B = 1

		if C == 0:
			C=1
		
		return 1 - A/(math.sqrt(B)*math.sqrt(C))



	def __str__(self):
		return str(self.row)
