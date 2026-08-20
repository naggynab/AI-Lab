import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])   # AND inputs
t = np.array([0,0,0,1]) 

w= np.zeros(2)
b = 0.0
lr = 0.1

for epoch in range (200):
    for xi , ti in zip(X , t):
        y_in = np.dot(w,xi) + b
        error = ti - y_in
        w += lr * error * xi
        b += lr * error 

print(w , b , epoch)

for xi in X:
    y_in = b + np.dot(w, xi)
    print(xi, "->", 1 if y_in > 0.5 else 0) 