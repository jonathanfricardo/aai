import numpy as np

class Layer:
    def __init__(self):
        pass
    def forward(self, input):
        pass
    def backward(self, grad_output, lr):
        pass


class ReLU(Layer):
    def forward(self, input):
        self.input = input
        return np.maximum(0, input)
    
    def backward(self, grad_output, lr):
        return grad_output * ( (self.input > 0) * 1)
  
class Sigmoid(Layer):
    def forward(self, input):
        self.output = 1/(1+np.exp(-input))
        return self.output
    
    def backward(self, grad_output, lr):
        return self.output * (1 - self.output) * grad_output

class Tanh(Layer):
    def forward(self, input):
        self.output = np.tanh(input)
        return self.output
    
    def backward(self, grad_output, lr):
        return (1 - self.output**2) * grad_output

class Dense(Layer):
    def __init__(self, input_units, output_units):
        self.Weights = np.random.randn(output_units, input_units)
        self.Bias = np.random.randn(output_units,1)
    
    def forward(self, input):
        self.input = input
        return self.Weights @ input + self.Bias
       
    def backward(self, grad_output, lr):
        grad_input = self.Weights.T @ grad_output
        grad_weights = grad_output @ self.input.T
        self.Weights -= lr * grad_weights
        self.Bias -= lr * grad_output
 
        return grad_input


    def print(self):
        print("Weights: ", self.Weights)
        print("Bias: ", self.Bias)


class Network:
    def __init__(self):
        self.layers = []
    
    def add(self, layer):
        self.layers.append(layer)
    
    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def backward(self, grad_output, lr):
        for layer in reversed(self.layers):
            grad_output = layer.backward(grad_output, lr)
        return grad_output  
    
    def train(self, X, Y, lr):
        output = self.forward(X)
        loss = np.sum((output - Y)**2)
        grad_output = 2*(output - Y)
        self.backward(grad_output, lr)
        return loss
    

# Path: main.py
def main():
    net = Network()
    net.add(Dense(2, 3))
    net.add(Tanh())
    net.add(Dense(3, 1))
    net.add(Tanh())
    
    X_arr = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
    Y_arr = np.reshape([[0], [1], [1], [0]], (4, 1, 1))    
    
    for i in range(10000):
        for X, Y in zip(X_arr, Y_arr):
            loss = net.train(X, Y, 0.1)
            if i % 100 == 0:
                print("Loss: ", loss)
    
    print(net.forward(X_arr[0]))
    print(net.forward(X_arr[1]))
    print(net.forward(X_arr[2]))
    print(net.forward(X_arr[3]))

main()