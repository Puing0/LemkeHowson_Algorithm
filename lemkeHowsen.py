################################################
#					methodes
################################################
# supprimer label et MAJ state
def dropLabel(plabel, qlabel, idx):
		global state
		if idx == 0:
			if plabel[state[0]][0]== 0:
				x = plabel[state[0]][1]
			else:
				x = plabel[state[0]][0]
				
			# chercher le label et MAJ
			value = [i for i in plabel if x in plabel[i] and i != state[0]]
			# print("value ",value)
			state = (value[0], state[1])
			# print(state)

		if idx == 1:
			if plabel[state[0]][0]== 1:
				x = plabel[state[0]][1]
			else:
				x = plabel[state[0]][0]
				
			# chercher le label et MAJ
			value = [i for i in plabel if x in plabel[i] and i != state[0]]
			# print(value)
			state = (value[0], state[1])
			# print(state)

		if idx == 2:
			if qlabel[state[1]][0]== 1:
				x = qlabel[state[1]][1]
			else:
				x = qlabel[state[1]][0]
				
			# chercher le label et MAJ
			value = [i for i in qlabel if x in qlabel[i] and i != state[1]]
			# print(value)
			state = (state[0], value[0])
			# print(state)

		if idx == 3:
			if qlabel[state[1]][0]== 3:
				x = qlabel[state[1]][1]
			else:
				x = qlabel[state[1]][0]
				
			# chercher le label et MAJ
			value = [i for i in qlabel if x in qlabel[i] and i != state[1]]
			# print(value)
			state = (state[0], value[0])
			# print(state)

# get commmon element 
def getCommonElt(state, plabel, qlabel):
	t1 = plabel[state[0]]
	t2 = qlabel[state[1]]

	return [elt for elt in t1 for elt2 in t2 if elt == elt2]

# get label 
def getLabel(state, plabel, qlabel):
	t1 = plabel[state[0]]
	t2 = qlabel[state[1]]
	return t1, t2

# get nash equilibrium and normalize it
def ENash(state, pcoord, qcoord):
	t1 = pcoord[state[0]]
	t2 = qcoord[state[1]]
	# normalisation 
	E1 = (t1[0]/(t1[0]+t1[1]) , t1[1]/(t1[0]+t1[1]))
	E2 = (t2[0]/(t2[0]+t2[1]) , t2[1]/(t2[0]+t2[1]))

	return E1, E2
		
		


################################################
#			Extracting polytopes
################################################

# importing libraries
from sympy import symbols, Eq, solve
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial

# defining symbols used in equations
# or unknown variables
x, y = symbols('x1,x2')

# defining equations
eq1 = Eq((3*x+y), 1)
eq2 = Eq((x+3*y), 1)

eq3 = Eq((1-3*y), 0)
eq4 = Eq((1-3*x), 0)

# solving the equation
sol1 =solve((eq1, eq2), (x, y))
sol2 =solve((eq3, eq4), (x, y))


V = [(0,0)]
V.append([0, sol2[y]])
V.append([sol2[x], 0])
V.append([sol1[x], sol1[y]])
V = np.array(V)
print("==========================================================")
print("\t \t \t POLYTOPES VECTOR")
print("==========================================================")
print("Vecteur des polytopes :",V)

#######################################################
#			Affichage
#######################################################

p = scipy.spatial.ConvexHull(V)
# plt.figure()
scipy.spatial.convex_hull_plot_2d(p)
plt.title("P")
plt.text(0.15, 0.02, '1')
plt.text(0.02, 0.15, '0')
plt.text(0.13, 0.27, '2')
plt.text(0.28, 0.10, '3')
plt.show()

q = scipy.spatial.ConvexHull(V)
# plt.figure()
scipy.spatial.convex_hull_plot_2d(q)
plt.title("Q")
plt.text(0.15, 0.02, '3')
plt.text(0.02, 0.15, '2')
plt.text(0.13, 0.27, '1')
plt.text(0.28, 0.10, '0')
plt.show()



##########################################################
#				Traitement
##########################################################

# definir les labels 

P_lab = {
	"a": [0, 1],
	"b": [1, 3], 
	"c": [3, 2], 
	"d": [0,2]
}

Q_lab = {
	"w": [3, 2],
	"x": [3, 0], 
	"y": [1, 0],
	"z": [1, 2]
}

# Definir les coordonnees

P_coord ={
	"a": V[0],
	"b": V[2], 
	"c": V[3], 
	"d": V[1]
}
Q_coord ={
	"w": V[0],
	"x": V[2], 
	"y": V[3], 
	"z": V[1]
}

# print(P_coord, Q_coord)

# label a supprimer 
sup_lab = 1
# initial state
state = ("a", "w")
print("==========================================================")
print("\t \t \t ITERATING THRO LABELS")
print("==========================================================")
# supprimer le premier label 
dropLabel(P_lab, Q_lab, sup_lab)
print("state", state)

t1, t2 = getLabel(state, P_lab, Q_lab)
result = tuple(set(t1+t2))

print("result ", result)

while result != (0, 1, 2, 3):
	x = getCommonElt(state, P_lab, Q_lab)
	print("next layer to drop ", x[0])

	print("drop ", x[0])
	print(state)
	dropLabel(P_lab, Q_lab, x[0])
	print("state ",state)
	t1, t2 = getLabel(state, P_lab, Q_lab)
	result = tuple(set(t1+t2))

	print("result ", result)

# cas P U Q = (0 1 2 3)
print("==========================================================")
print("\t \t \t NASH EQUILIBRIUM ")
print("==========================================================")
print("NASH EQUILIBRIUM AT ", state)
res1 , res2 = ENash(state, P_coord, Q_coord)
print("NE IS : ", res1, res2)

#######################################################
# 					Tester librairie
#######################################################

import nashpy as nash 
a = [[3, 1], [1, 3]]
b = [[1, 3], [3, 1]]
g = nash.Game(a, b)
print("==========================================================")
print("\t \t \t LIBRARY RESULTS")
print("==========================================================")

print(list(g.lemke_howson_enumeration()))