from Question1 import Board, solveBFS
from Question3 import fun, fun_for_max
from scipy import optimize
import numpy as np


def main():

	
	#QUESTION 3
	xnot = list(range(0,11))
	myarray = np.asarray(xnot)
	deltaX = np.arange(0,0.11,0.01)
	res = optimize.fminbound(fun_for_max,0,10)
	print(res)

	






if __name__ == "__main__":
	main()