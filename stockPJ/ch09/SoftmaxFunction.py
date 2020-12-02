import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

print(softmax([1, 2, 3]))
print(softmax([4, 5, 6]))