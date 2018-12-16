import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 1, 2, 3, 4, 3, 4, 6, 4])
y = np.array([2, 1, 0.5, 1, 3, 3, 2, 5, 4])

 def Y_0(x, t0, t1):
        return t0 + t1 * x

def cost_func(t0, t1):
    t0 = np.asarray(t0)
    t1 = np.asarray(t1)
    return np.average((y-Y_0(x, t0, t1))**2, axis=2)

N = 10
a = 0.1
t0 = [np.array((0,0))]
t1 = [np.array((0,0))]
def learn(t0,t1,a,N,x,y):
    t0_new = t0
    t1_new = t1
    for i in range(N-1):
        for j in range(len(x)):
        t0_new = t0_new - 2*a / len(x)*np.sum(Y_0(x[j],t0_new,t1_new) - y[j])
        t1_new = t1_new - 2*a / len(x)*np.sum((Y_0(x[j],t0_new,t1_new) - y[j])*x[j])
        print(cost_func(t0_new, t1_new))
    return t0_new, t1_new
print(learn(t0,t1,a,N,x,y))
