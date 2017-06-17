# Kevin Loi
# kloi
# pa7
# functions that perform standard vector operations

"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""
#------------------------------------------------------------------------------
# import standard library modules
#------------------------------------------------------------------------------
import math
import random

#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------
def add(u, v):
	w = []
	for i in range(len(u)):
		w.append(u[i]+v[i])
	return w
# end add()

def negate(u):
	w = []
	for i in range(len(u)):
		neg = u[i]*-1
		w.append(neg)
	return w
# end negate()   

def sub(u, v):
	w = []
	for i in range(len(u)):
		w.append(u[i]-v[i])
	return w
# end sub()

def scalarMult(c, u):
	w = []
	for i in range(len(u)):
		mult = c*u[i]
		w.append(mult)
	return w
# end scalarMult()

def zip(u, v):
	w = []
	for i in range(len(u)):
		w.append(u[i]*v[i])
	return w
# end zip()

def dot(u, v):
	sum = 0
	w = zip(u, v)
	for i in range(len(w)):
		sum += w[i]
	return sum
# end dot()

def length(u):
	sum = 0
	for i in range(len(u)):
		sum += (u[i])**2
	root = math.sqrt(sum)
	return root
# end length()
   
def unit(v):
	w = []
	l = length(v)
	for i in range(len(v)):
		w.append(v[i]/l)
	return w
# end unit()

def angle(u, v):
   """
   Return the angle (in degrees) between vectors u and v.
   """
   return math.degrees(math.acos(dot(unit(u),unit(v))))
# end angle()

def randVector(n, a, b):
	w = []
	for i in range(n):
		w.append(a+(b-a)*random.random())
	return w
# end randomVector()


   