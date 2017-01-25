
from  collections import deque
import networkx as nx
import numpy as np 
from random import randint

class Board():
	def __init__(self,matrix=None):
		self.goal = np.zeros((2,3))
		self.goal[0,0] = 0
		self.goal[0,1] = 1
		self.goal[0,2] = 2
		self.goal[1,0] = 3
		self.goal[1,1] = 4
		self.goal[1,2] = 5
		if matrix is None:
			self.matrix = np.zeros((2,3))
			self.matrix[0,0] = 5
			self.matrix[0,1] = 1
			self.matrix[0,2] = 0
			self.matrix[1,0] = 4
			self.matrix[1,1] = 3
			self.matrix[1,2] = 2
		else:
			self.matrix = matrix

	def __str__(self):
		return np.array_str(self.matrix)

	def getMatrix(self):
		return self.matrix
	def getGoal(self):
		return self.goal

	def hamming(self):
		self.hamming = 0
		for i in range(1,2):
			for j in range(1,3):
					if self.matrix[i,j] != self.goal[i,j]:
						self.hamming += 1
		return self.hamDistance

	def manhattan(self):
		self.manDistance = 0
		for i in range(1,2):
			for j in range(1,3):
					if self.matrix[i,j] != self.goal[i,j]:
						self.manDistance += i+j
		return self.manDistance 

def solveBFS(board):
	visited = set()
	searchGraph = nx.Graph() 
	pQueue = deque() #use append and pop for FIFO
	pQueue.append(board)
	while pQueue:
		vertex = pQueue.pop(0)
		v = vertex.getMatrix()
		if vertex not in visited: #comparison doesn't work
			visited.add(vertex)
			free = np.where(v==0)
			ii = free[0]
			jj = free[1]
			i = ii.item(0)
			j = jj.item(0)
			#generate next nodes, 6 ugly cases
			#FIRST COLUMN
			if i==0 and j==0:
				m = np.copy(v) # reminder: v is matrix of vertex
				n = np.copy(v)
				m[i,j] = n[i,j] = 0
				m[i+1,j] = v[i,j]
				n[i,j+1] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)
			if i==1 and j==0:
				m = np.copy(v)
				n = np.copy(v)
				m[i,j] = n[i,j] = 0
				m[i-1,j] = v[i,j]
				n[i,j+1] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)
			
			#SECOND COLUMN
			if i==0 and j==1:
				m = np.copy(v)
				n = np.copy(v)
				p = np.copy(v)
				m[i,j-1] = v[i,j]
				n[i,j+1] = v[i,j]
				p[i+1,j] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pBoard = Board(p)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_node(pBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)
				searchGraph.add_edge(vertex,pBoard)
			if i==1 and j==1:
				m = np.copy(v)
				n = np.copy(v)
				p = np.copy(v)
				m[i,j] = n[i,j] = p[i,j] = 0
				m[i,j-1] = v[i,j]
				n[i,j+1] = v[i,j]
				p[i-1,j] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pBoard = Board(p)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				pQueue.append(pBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_node(pBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)
				searchGraph.add_edge(vertex,pBoard)

			#THIRD COLUMN
			if i==0 and j==2:
				m = np.copy(v)
				n = np.copy(v)
				m[i,j] = n[i,j] = 0
				m[i+1,j] = v[i,j]
				n[i,j-1] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)
			if i==1 and j==2:
				m = np.copy(v)
				n = np.copy(v)
				m[i,j] = n[i,j] = 0
				m[i-1,j] = v[i,j]
				n[i,j-1] = v[i,j]
				mBoard = Board(m)
				nBoard = Board(n)
				pQueue.append(mBoard)
				pQueue.append(nBoard)
				searchGraph.add_node(mBoard)
				searchGraph.add_node(nBoard)
				searchGraph.add_edge(vertex,mBoard)
				searchGraph.add_edge(vertex,nBoard)

	return visited, searchGraph








			


			



 











