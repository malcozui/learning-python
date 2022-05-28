import math

softmax_output = [0.7, 0.1, 0.2]
target_outout = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_outout[0] +
         math.log(softmax_output[0]) * target_outout[0] +
         math.log(softmax_output[0]) * target_outout[0])
print(loss)