import numpy as np
from rubik import Rubik
import random
import os
from keras import layers
from keras.layers import Input,  Dense, Activation, BatchNormalization, Flatten
from keras.models import Sequential, Model, model_from_json
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
import keras
import keras.backend as K


def random_data_set_generation(c,n):
	moves_Y = []
	cube_X = []
	while n:	
		m = random.randint(0,11)
		n-=1
		Y = np.zeros(12)
		# print(Y.shape)
		Y[c.reverse_move[m]] = 1
		moves_Y.append(Y)
		c.move(c.moveCharList[m])
		cube_X.append(np.array(c.cube).flatten())
		# c.display(c.cube)
	print("Cube Random Data Generated")
	return np.array(cube_X), np.array(moves_Y)

def model(input_shape):
    # Define the input placeholder as a tensor with shape input_shape. Think of this as your input image!
    X_input = Input(input_shape)

    # Zero-Padding: pads the border of X_input with zeroes
    X = ZeroPadding2D((3, 3))(X_input)

    # CONV -> BN -> RELU Block applied to X
    X = Conv2D(32, (7, 7), strides = (1, 1), name = 'conv0')(X)
    X = BatchNormalization(axis = 3, name = 'bn0')(X)
    X = Activation('relu')(X)

    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool')(X)

    # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
    X = Flatten()(X)
    X = Dense(1, activation='sigmoid', name='fc')(X)

    # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
    model = Model(inputs = X_input, outputs = X, name='HappyModel')

    return model


c = Rubik()
# param = init_params(n1,n2)

number_data = 1000000

inp, out = random_data_set_generation(c,number_data)

X_train , X_test = inp[:int(number_data*0.9)] , inp[int(number_data*0.9):]
Y_train , Y_test = out[:int(number_data*0.9)] , out[int(number_data*0.9):]
print(X_train.shape,X_test.shape)
print(Y_train.shape,Y_test.shape)
model = Sequential()
if(not __debug__):
	model.add(Dense(26, input_dim=54, activation='relu'))
	model.add(Dense(20, activation='relu'))
	model.add(Dense(17, activation='relu'))
	model.add(Dense(12, activation='softmax'))
	lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=1e-2, decay_steps=10000, decay_rate=0.9)
	optimizer = keras.optimizers.SGD(learning_rate=lr_schedule)
	model.compile(loss='mean_squared_error', optimizer=optimizer, metrics=['accuracy'])

	model.fit(X_train, Y_train, epochs=500, batch_size=100)

	_, accuracy = model.evaluate(X_test, Y_test)
	print('Accuracy: %.2f' % (accuracy*100))
else:
	model = load_model('model.h5')
	model.fit(X_train, Y_train, epochs=300, batch_size=200)
# param = init_params(n1,n2)
# epoch = 1000
# for i in range(epoch):
# 	AL, caches = L_model_forward(inp, param)

# 	grads = L_model_backward(AL,out,caches)

# 	param = update_parameters(param,grads, 0.1)
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
 
# later...
 
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
# c.maybe()
# print(param)