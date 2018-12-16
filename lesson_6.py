import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]



def E(x, k, b, y):
    return (y - (k*x + b))**2

def J(x, k, b, y):
    sum = 0
    for i in range(len(x)):
        sum += E(x[i], k, b, y[i])
    return sum/len(x)

x = [1, 1, 2, 3, 4, 3, 4, 6, 4]
y = [2, 1, 0.5, 1, 3, 3, 2, 5, 4]
k = 0
b = 0
l=0.1
N=10

print(J(x, k, b, y))



def learn(k,b,l,N,x,y):
    bnew=b
    knew=k
    for i in range(N):
        knew = knew - 2 * l / len(x) + sum([ (y[j] - k * x[j] - b) * x[j]  for j in range(len(x))])
        bnew = bnew - 2 * l / len(x) + sum([ (y[j] - k * x[j] - b)  for j in range(len(x))])
        print(J(x, knew, bnew, y))
    return knew,bnew
print(learn(x, k, l, b,  N, y))

N = 5
alpha = 0.1
theta = [np.array((0,0))]
J = [J(*theta[0])[0]]
for j in range(N-1):
    last_theta = theta[-1]
    this_theta = np.empty((2,))
    this_theta[0] = last_theta[0] - alpha / len(x) * np.sum(
                                    (hypothesis(x, *last_theta) - y))
    this_theta[1] = last_theta[1] - alpha / len(x) * np.sum(
                                    (hypothesis(x, *last_theta) - y) * x)
    theta.append(this_theta)
    J.append(J(*this_theta))


#######################################################################################

    def hypothesis(x, theta0, theta1):
        return theta0 + theta1 * x

def cost_func(theta0, theta1):
    theta0 = np.atleast_3d(np.asarray(theta0))
    theta1 = np.atleast_3d(np.asarray(theta1))
    return np.average((y-hypothesis(x, theta0, theta1))**2, axis=2)

x = np.array([1, 1, 2, 3, 4, 3, 4, 6, 4])
y = np.array([2, 1, 0.5, 1, 3, 3, 2, 5, 4])

N = 10
alpha = 0.1
theta = [np.array((0,0))]
J = [cost_func(*theta[0])[0]]
for j in range(N-1):
    last_theta = theta[-1]
    this_theta = np.empty((2,))
    this_theta[0] = last_theta[0] - alpha / len(x) * np.sum(
                                    (hypothesis(x, *last_theta) - y))
    this_theta[1] = last_theta[1] - alpha / len(x) * np.sum(
                                    (hypothesis(x, *last_theta) - y) * x)
    theta.append(this_theta)
    J.append(cost_func(*this_theta))


J


