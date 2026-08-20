import numpy as np
np.random.seed(2)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
t = np.array([[0],[1],[1],[0]])

def sig(x):
    return x / (1 + np.exp(-x))
def dsig(x):
    return x * (1-x)

W1 = np.random.uniform(-1,1,(2,4))
b1 = np.zeros((1,4))
W2 = np.random.uniform(-1,1,(4,1))
b2 = np.zeros((1,1))
lr = 0.5

for epoch in range(10000):
    #forward
    z = sig( X.dot(W1) +  b1)
    y = sig( z.dot(W2) + b2)
    #backward
    dk = (t - y) * dsig(y)
    d = dk.dot(W2.T)
    dj = d * dsig(z)
    #weights
    W2 += z.T.dot(dk) * lr
    b2 = np.sum(dk , axis = 0 , keepdims=True )
    W1 += X.T.dot(dj) * lr
    b1 = np.sum(dj , axis = 0 , keepdims= True)

#prediction
for xi , ti in zip(X , t):
    pred_y =     sig( (sig(xi.dot(W1) + b1)).dot(W2) + b2 )
    print(xi , pred_y[0][0] , ti[0])