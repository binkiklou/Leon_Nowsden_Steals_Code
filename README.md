Hello.
# WTF IS THAT
Ok so this is not my crappy code, it´s leon´s nowsden ugly code. he litteraly stole it and i keep this repo as a propf
# 1.Step

a)Install Python 3.5.x
b) open CMD 
c) type in "pip3 install numpy"

# Training process
Training process

But how do we teach our neuron to answer the question correctly? We will give each input a weight, which can be a positive or negative number. An input with a large positive weight or a large negative weight, will have a strong effect on the neuron’s output. Before we start, we set each weight to a random number. Then we begin the training process:

Take the inputs from a training set example, adjust them by the weights, and pass them through a special formula to calculate the neuron’s output.
Calculate the error, which is the difference between the neuron’s output and the desired output in the training set example.
Depending on the direction of the error, adjust the weights slightly.
Repeat this process 10, 000 times.


Eventually the weights of the neuron will reach an optimum for the training set. If we allow the neuron to think about a new situation, that follows the same pattern, it should make a good prediction.

This process is called back propagation.

# Formula for calculating the neuron’s output
You might be wondering, what is the special formula for calculating the neuron’s output? First we take the weighted sum of the neuron’s inputs, which is:


Next we normalise this, so the result is between 0 and 1. For this, we use a mathematically convenient function, called the Sigmoid function:


If plotted on a graph, the Sigmoid function draws an S shaped curve.

Thanks for reading. Leon Nowsden aka theAIKid

