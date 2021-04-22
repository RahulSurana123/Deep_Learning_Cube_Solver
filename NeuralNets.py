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
import tensorflow as tf
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

def custom_loss(y_actual, y_predicted):
	custom_loss_val = K.mean(K.sum(K.square((y_actual - y_predicted)/10)))
	return custom_loss_val 


c = Rubik()
# param = init_params(n1,n2)

number_data = 1000000

inp, out = random_data_set_generation(c,number_data)

X_train , X_test = inp[:int(number_data*0.9)] , inp[int(number_data*0.9):]
Y_train , Y_test = out[:int(number_data*0.9)] , out[int(number_data*0.9):]
print(X_train.shape,X_test.shape)
print(Y_train.shape,Y_test.shape)
model = Sequential()
model.add(Dense(54, input_dim=54, activation='relu'))
model.add(Dense(26, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(17, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(12, activation='softmax'))
lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=1.0, decay_steps=10000, decay_rate=0.1)
optimizer = keras.optimizers.RMSprop(0.001)
l = tf.keras.losses.CategoricalCrossentropy(
    from_logits=False,
    label_smoothing=0,
    reduction="auto",
    name="categorical_crossentropy",
)
model.compile(loss= l, optimizer= optimizer, metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=1000, batch_size=100000)

_, accuracy = model.evaluate(X_test, Y_test)
print('Accuracy: %.2f' % (accuracy*100))