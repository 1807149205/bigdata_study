import numpy as np

def tanh(x):
    return np.tanh(x)

def softmax(x):
    # 求指数
    exp = np.exp(x)
    return exp / exp.sum

dimensions = [28*28, 10]

# tanh函数和softMax都为归一化函数
activation = [tanh, softmax]