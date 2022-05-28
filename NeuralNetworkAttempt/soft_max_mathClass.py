import numpy as np
# the combination of exponentiation and normalisation is whta makes the soft max function
layer_outputs = [4.8, 1.21, 2.385]

E = np.e
# first we exponentiate all the outputs
exp_values = np.exp(layer_outputs)
# then we divide every value by the sum of all the exponents to get the part of 1 they make up in whole.
norm_values = exp_values / np.sum(exp_values)

print(norm_values)
print(sum(norm_values))