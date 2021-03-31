from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import Rubik

model = Sequential()
model.add(Dense(27, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(12, activation='relu'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))