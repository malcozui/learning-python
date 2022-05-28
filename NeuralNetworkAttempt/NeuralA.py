import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
# this is the spiral data function.
'''
def create_data(points, classes):
  X = np.zeros((points * classes), 2)
  y = np.zeros(points * classes, dtype='uint8')
  for class_number in range(classes):
    ix = range(points * class_number, points * (class_number + 1))
    r = np.linspace(0.0, 1, points)
    t = np.linspace(class_number * 4, (class_number + 1) * 4, points) + np.random.randn(points) * 0.2
    X[ix] = np.c_[r * np.sin(t * 2.5), r * np.cos(t * 2.5)]
    y[ix] = class_number
  return X, y
'''

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

X, y = spiral_data(100, 3)

class Layer_Dense:
  def __init__(self, n_inputs, n_neurons):
    # Weights are multiplied by 0.10 to keep them in range -1 < x < 1
    # we pick a matrix of random weights with the height being the neurons count and the width being the inputs count, we generate the array transposed beforehand
    self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
  def forward(self, inputs):
    self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
  # Activation function using rectified linear equasion { x <= 0 == 0; x > 0 == x}
  def forward(self, inputs):
    self.output = np.maximum(0, inputs)
    #applies the ReLU to the inputs

layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()

layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)
