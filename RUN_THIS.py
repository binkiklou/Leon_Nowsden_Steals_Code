#Download the code from https://github.com/TheAIKid/NeuralNet_in_9_Lines_of_CODE
#Copy it to your repo
#Brag about it
# Importation of the libraries

from numpy import exp, array, random, dot
# Define our data
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
# Using stuff
random.seed(1)
# Maths that you dont fucking understand
synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
avr = 1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights))))
# This shows our result
print("Our result is Vsauce michael here")





