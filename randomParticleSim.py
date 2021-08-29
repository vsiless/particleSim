#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy import  stats
# Function definition is here
def simulation1( size ):
	x=0
	y=0
	iteration =0
	while  x!= size and y!= size:
		directions=[]
		if x>0:
			directions.append(0)
		if x< size:
			directions.append(1)
		if y>0:
			directions.append(2)
		if y< size:
			directions.append(3)
		nextDir = np.random.randint(len(directions))
		if directions[nextDir]==0:
			x-=1
		if directions[nextDir]==1:
			x+=1
		if directions[nextDir]==2:
			y-=1
		if directions[nextDir]==3:
			y+=1
		iteration+=1
	return iteration
def simulation2( size ):
	x=0
	y=0
	iteration =0
	while  x!= size and y!= size:
		nextDir = np.random.randint(4)
		if nextDir==0 and x>0:
			x-=1
		if nextDir==1 and x<size:
			x+=1
		if nextDir==2 and y>0:
			y-=1
		if nextDir==3 and y< size:
			y+=1
		iteration+=1
	return iteration
def simulation3( size ):
	x=0
	y=0
	iteration =0
	while  x!= size and y!= size:
		nextDir = np.random.randint(4)
		if nextDir==0:
			x+= -1 if x>0 else +1
		if nextDir==1:
			x+= +1 if x<size else -1
		if nextDir==2:
		 	y+= -1 if  y>0 else +1
		if nextDir==3:
			y+= +1 if y< size else -1
		iteration+=1
	return iteration
def simulate(maxN, simN, simFunc):
	y=[]			
	yerr=[]
	for i in range(maxN):
		val=[]
		for j in range(simN):
			val.append(simFunc(i))
		y.append(np.mean(val))
		yerr.append(stats.sem(val))
	return y, yerr

maxN=11
simN=5000
y, yerr =simulate(maxN, simN, simulation1)
print("Excercise 1)a- mean:" , y , " sem ", yerr) 
plt.errorbar(range(maxN),y,yerr, label="1-only possible directions")
y, yerr =simulate(maxN, simN, simulation2)
print("Excercise 2)a- mean:" , y , " sem ", yerr) 
plt.errorbar(range(maxN),y,yerr, label="2-all directions, move only when possible")
y, yerr =simulate(maxN, simN, simulation3)
plt.errorbar(range(maxN),y,yerr, label="3-all directions, bounce back when not possible")
print("Excercise 3)a- mean:" , y , " sem ", yerr) 
plt.legend()
plt.show()
