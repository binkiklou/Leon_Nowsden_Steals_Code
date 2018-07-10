# Import our libs
from numpy import exp, array, random, dot
# Define our data
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
# Use our lib 
random.seed(1)
# We do maths 
synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
avr = 1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights))))
# This shows our result
print("Our result is",avr)





