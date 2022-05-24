# This is a tutorial series I'm following on YT by sentdex
# my goal is to learn how neural networks work, and theoretically i should
# be able to do this in another lang I'm more comfortable with as well like C#

inputs = [1, 2, 3, 2.5]

weights = [
            [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]
            ]
biases = [2, 3, 0.5]

layer_ouputs = [] # output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # output of current nueron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_ouputs.append(neuron_output)

print(layer_ouputs)