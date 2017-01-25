import numpy as np
from scipy import optimize
from IPython.core.debugger import Tracer

def fun(x):
	return (np.cos(x*x/2))/np.log2(x+2)

def fun_for_max(x):
	return -fun(x)

#range as array, start scalar
def hillClimbing(fun,start,constraint,delta)

	left = copy(constraint[0]) #might use recursion
	right = copy(constraint[1])

	#let us not start at the edges
	if x not in set(left,right):
		neighbor1 = start+delta
		neighbor2 = start-delta
		if neighbor1 <= right and neighbor2 >= left :

			if fun(neighbor1) > fun(neighbor2):
				neo = neighbor1
			if fun(neighbor1) < fun(neighbor2):
				neo = neighbor2
			if fun(neighbor1) == fun(neighbor2): #tiebreak, inf loop?
				neo = neighbor1


		

