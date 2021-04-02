import numpy as np
from rubik import Rubik
import random


def random_data_set_generation(c,n):
	moves_Y = []
	cube_X = []
	while n:	
		m = random.randint(0,11)
		n-=1
		moves_Y.append(c.reverse_move[m])
		c.move(c.moveCharList[m])
		cube_X.append(np.array(c.cube).flatten())
		# c.display(c.cube)
	print("Cube Random Data Generated")
	return cube_X, moves_Y


def softmax(vec):

	for i in range(len(vec)):
		vec[i] = vec[i] / sum(vec)

	return vec

#
#    Init Weights for a 3 layer with n1 n2 12 Layers 12 is Output Layer
#

def init_params(n1,n2):
	np.random.seed(1)
	Params = {}
	Params['W0'] = np.random.rand(n1,54)
	Params['W1'] = np.random.rand(n2,n1)
	Params['W2'] = np.random.rand(12,n2)
	Params['B0'] = np.zeros(n1,1)
	Params['B1'] = np.zeros(n2,1)
	Params['B2'] = np.zeros(12,1)
	
	return Params

def linear_forward(A, W, b):
	"""
	Implement the linear part of a layer's forward propagation.

	Arguments:
	A -- activations from previous layer (or input data): (size of previous layer, number of examples)
	W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
	b -- bias vector, numpy array of shape (size of the current layer, 1)

	Returns:
	Z -- the input of the activation function, also called pre-activation parameter 
	cache -- a python dictionary containing "A", "W" and "b" ; stored for computing the backward pass efficiently
	"""
	
	### START CODE HERE ### (≈ 1 line of code)
	Z = np.dot(W, A) + b
	### END CODE HERE ###
	
	assert(Z.shape == (W.shape[0], A.shape[1]))
	cache = (A, W, b)
	
	return Z, cache

def linear_activation_forward(A_prev, W, b, activation):
	"""
	Implement the forward propagation for the LINEAR->ACTIVATION layer

	Arguments:
	A_prev -- activations from previous layer (or input data): (size of previous layer, number of examples)
	W -- weights matrix: numpy array of shape (size of current layer, size of previous layer)
	b -- bias vector, numpy array of shape (size of the current layer, 1)
	activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"

	Returns:
	A -- the output of the activation function, also called the post-activation value 
	cache -- a python dictionary containing "linear_cache" and "activation_cache";
			 stored for computing the backward pass efficiently
	"""
	
	if activation == "sigmoid":
		# Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
		### START CODE HERE ### (≈ 2 lines of code)
		Z, linear_cache = linear_forward(A_prev, W, b)
		A, activation_cache = sigmoid(Z)
		### END CODE HERE ###
	
	elif activation == "relu":
		# Inputs: "A_prev, W, b". Outputs: "A, activation_cache".
		### START CODE HERE ### (≈ 2 lines of code)
		Z, linear_cache = linear_forward(A_prev, W, b)
		A, activation_cache = relu(Z)
		### END CODE HERE ###
	
	assert (A.shape == (W.shape[0], A_prev.shape[1]))
	cache = (linear_cache, activation_cache)

	return A, cache

def L_model_forward(X, parameters):
	"""
	Implement forward propagation for the [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID computation
	
	Arguments:
	X -- data, numpy array of shape (input size, number of examples)
	parameters -- output of initialize_parameters_deep()
	
	Returns:
	AL -- last post-activation value
	caches -- list of caches containing:
				every cache of linear_relu_forward() (there are L-1 of them, indexed from 0 to L-2)
				the cache of linear_sigmoid_forward() (there is one, indexed L-1)
	"""

	caches = []
	A = X
	L = len(parameters) // 2                  # number of layers in the neural network
	
	# Implement [LINEAR -> RELU]*(L-1). Add "cache" to the "caches" list.
	for l in range(1, L):
		A_prev = A 
		### START CODE HERE ### (≈ 2 lines of code)
		A, cache = linear_activation_forward(A_prev, 
											 parameters['W' + str(l)], 
											 parameters['b' + str(l)], 
											 activation='relu')
		caches.append(cache)
		
		### END CODE HERE ###
	
	# Implement LINEAR -> SIGMOID. Add "cache" to the "caches" list.
	### START CODE HERE ### (≈ 2 lines of code)
	AL, cache = linear_activation_forward(A, 
										  parameters['W' + str(L)], 
										  parameters['b' + str(L)], 
										  activation='sigmoid')
	caches.append(cache)
	
	### END CODE HERE ###
	
	assert(AL.shape == (1, X.shape[1]))
			
	return AL, caches

def compute_cost(AL, Y):
	"""
	Implement the cost function defined by equation (7).

	Arguments:
	AL -- probability vector corresponding to your label predictions, shape (1, number of examples)
	Y -- true "label" vector (for example: containing 0 if non-cat, 1 if cat), shape (1, number of examples)

	Returns:
	cost -- cross-entropy cost
	"""
	
	m = Y.shape[1]

	# Compute loss from aL and y.
	### START CODE HERE ### (≈ 1 lines of code)
	cost = (-1 / m) * np.sum(np.multiply(Y, np.log(AL)) + np.multiply(1 - Y, np.log(1 - AL)))
	### END CODE HERE ###
	
	cost = np.squeeze(cost)      # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
	assert(cost.shape == ())
	
	return cost

def linear_backward(dZ, cache):
	"""
	Implement the linear portion of backward propagation for a single layer (layer l)
Arguments:
	dZ -- Gradient of the cost with respect to the linear output (of current layer l)
	cache -- tuple of values (A_prev, W, b) coming from the forward propagation in the current layer
Returns:
	dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
	dW -- Gradient of the cost with respect to W (current layer l), same shape as W
	db -- Gradient of the cost with respect to b (current layer l), same shape as b
	"""
	A_prev, W, b = cache
	m = A_prev.shape[1]
	dW = 1./m * np.dot(dZ,A_prev.T)
	db = 1./m * np.sum(dZ, axis = 1, keepdims = True)
	dA_prev = np.dot(W.T,dZ)
	
	assert (dA_prev.shape == A_prev.shape)
	assert (dW.shape == W.shape)
	assert (db.shape == b.shape)
	
	return dA_prev, dW, db

def sigmoid(Z):
	
	A = 1/(1+np.exp(-Z))
	cache = Z
	
	return A, cache

def relu_backward(dA, cache):
	"""
	Implement the backward propagation for a single RELU unit.
Arguments:
	dA -- post-activation gradient, of any shape
	cache -- 'Z' where we store for computing backward propagation efficiently
Returns:
	dZ -- Gradient of the cost with respect to Z
	"""
	
	Z = cache
	dZ = np.array(dA, copy=True) # just converting dz to a correct object.
	
	# When z <= 0, you should set dz to 0 as well. 
	dZ[Z <= 0] = 0
	
	assert (dZ.shape == Z.shape)
	
	return dZ

def sigmoid_backward(dA, cache):
	"""
	Implement the backward propagation for a single SIGMOID unit.
Arguments:
	dA -- post-activation gradient, of any shape
	cache -- 'Z' where we store for computing backward propagation efficiently
Returns:
	dZ -- Gradient of the cost with respect to Z
	"""
	
	Z = cache
	
	s = 1/(1+np.exp(-Z))
	dZ = dA * s * (1-s)
	
	assert (dZ.shape == Z.shape)
	
	return dZ

def tanh_backward(dA, cache):
	"""
	Implement the backward propagation for a single RELU unit.
Arguments:
	dA -- post-activation gradient, of any shape
	cache -- 'Z' where we store for computing backward propagation efficiently
Returns:
	dZ -- Gradient of the cost with respect to Z
	"""
	
	Z = cache
	s,_ = tanh(Z)
	dZ = dA * (1-s**2)
	assert (dZ.shape == Z.shape)
	
	return dZ

def linear_activation_backward(dA, cache, activation):
	"""
	Implement the backward propagation for the LINEAR->ACTIVATION layer.
	
	Arguments:
	dA -- post-activation gradient for current layer l 
	cache -- tuple of values (linear_cache, activation_cache) we store for computing backward propagation efficiently
	activation -- the activation to be used in this layer, stored as a text string: "sigmoid" or "relu"
	
	Returns:
	dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
	dW -- Gradient of the cost with respect to W (current layer l), same shape as W
	db -- Gradient of the cost with respect to b (current layer l), same shape as b
	"""
	linear_cache, activation_cache = cache
	
	dZ = sigmoid_backward(dA, activation_cache)
	A_prev, dW, db = linear_backward(dZ, linear_cache)
	
	return dA_prev, dW, db


def L_model_backward(AL, Y, caches):
	"""
	Implement the backward propagation for the [LINEAR->RELU] * (L-1) -> LINEAR -> SIGMOID group
	
	Arguments:
	AL -- probability vector, output of the forward propagation (L_model_forward())
	Y -- true "label" vector (containing 0 if non-cat, 1 if cat)
	caches -- list of caches containing:
				every cache of linear_activation_forward() with "relu" (there are (L-1) or them, indexes from 0 to L-2)
				the cache of linear_activation_forward() with "sigmoid" (there is one, index L-1)
	
	Returns:
	grads -- A dictionary with the gradients
			 grads["dA" + str(l)] = ... 
			 grads["dW" + str(l)] = ...
			 grads["db" + str(l)] = ... 
	"""
	grads = {}
	L = len(caches) # the number of layers
	m = AL.shape[1]
	Y = Y.reshape(AL.shape) # after this line, Y is the same shape as AL
	# Initializing the backpropagation
	dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
	# Lth layer (SIGMOID -> LINEAR) gradients. Inputs: "AL, Y, caches". Outputs: "grads["dAL"], grads["dWL"], grads["dbL"]
	current_cache = caches[L-1]
   # print('should be one',len(current_cache))
	grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache, activation = "sigmoid")
	for l in reversed(range(L-1)):
		# lth layer: (RELU -> LINEAR) gradients.
		current_cache = caches[l]
	  #  print('shoub be two',len(current_cache))
		dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA" + str(l + 1)], current_cache, activation = "relu")
		grads["dA" + str(l)] = dA_prev_temp
		grads["dW" + str(l + 1)] = dW_temp
		grads["db" + str(l + 1)] = db_temp
	return grads


#inputs
x = 54

# Layers 
n1 = 26
n2 = 3 

# Output
y = 12
c = Rubik()
# param = init_params(n1,n2)
inp,out = random_data_set_generation(c,1000)

c.maybe()
print(inp,out)