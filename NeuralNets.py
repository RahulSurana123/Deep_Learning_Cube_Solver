import numpy as np
from rubik import Rubik
import random

def random_data_set_generation(n):
	c = Rubik()
	moves_Y = []
	cube_X = []
	while n:	
		m = random.randint(0,11)
		n-=1
		moves_Y.append(c.reverse_move[m])
		c.move(c.moveCharList[m])
		cube_X.append(np.array(c.cube).flatten())
	return cube_X, moves_Y

inp,out = random_data_set_generation(1000)	

print(inp,out)


def softmax(vec):

	for i in range(len(vec)):
		vec[i] = vec[i] / sum(vec)

	return vec
