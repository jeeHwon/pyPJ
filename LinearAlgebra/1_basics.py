import numpy as np

# column vector
c = np.array([1,2,3])
print(c.shape)

# obataining a particular entry
print(c[0])

# row vector
r = np.array([ [1,2,3] ])
print(r.shape)

#obtaining a particular entry
print(r[0,1])

# creating a matrix with all zeros
a = np.zeros((2,2))
print(a)

# creating a matrix with all ones
b = np.ones((2,2))
print(b)

# creating a matrix filled with the same constant
c = np.full((2,2), 7)
print(c)

# creating a matrix with random values
d = np.random.random((2,2))
print(d)

# creating a matrix
A = np.array([[1,2],[3,4],[5,6]])
print(A)

# creating another matrix
B = np.array([[11,12,13,14],[15,16,17,18]])
print(B)

# transpose a matrix
A.T

# matrix-matrix multiplication
np.dot(A,B)

# coefficient matrix A and a vector b
A = np.array([[60, 5.5, 1],[65, 5.0, 0],[55, 6.0, 1]])
b = np.array([66,70,78])
print(A)
print(b)

# identity matrix
eye3 = np.eye(3)

# computing an inverse
from numpy.linalg import inv
A_inv = inv(A)

# wrong matrix multiplication
A_inv = inv(A)

# correct matrix multiplication
A.dot(A_inv)

# solution of a linear system
x = A_inv.dot(b)

# a better way to solve the same linear system
from numpy.linalg import solve
x = solve(A,b)