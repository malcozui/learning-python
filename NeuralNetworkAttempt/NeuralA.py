import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
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
class Activation_Softmax:
  def forward(self, inputs):
    exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
    probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
    self.output = probabilities
class Loss:
  def calculate(self, output, y):
    sample_losses = self.forward(output, y)
    data_loss = np.mean(sample_losses)
    return data_loss
class Loss_CatergoricalCrossEntropy(Loss):
  def forward(self, y_pred, y_true):
    samples = len(y_pred)
    y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
    if len(y_true.shape) == 1:
      correct_confidences = y_pred_clipped[range(samples), y_true]
    elif len(y_true.shape) == 2:
      correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
    negative_log_likelihoods = -np.log(correct_confidences)
    return negative_log_likelihoods

X, y = spiral_data(samples = 100, classes = 3)

dense1 = Layer_Dense(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

loss_function = Loss_CatergoricalCrossEntropy()
loss = loss_function.calculate(activation2.output, y)

print("Loss: ", loss)

# At this point I'd add an optimiser but i dont know how and sendex havent made a video on it yet, sad.