from numpy import *
import numpy as np
import time

time_start=time.time()
n = 4
a = np.random.rand(n,n)*20
c = np.linalg.inv(a)
b = np.ones(n)
d = np.linalg.solve(a,b) 
k = 0
i = 0
j = 0
print (d)
while i<n :
    while j<n :
        if a[i][j]>2 and a[i][j]<20 and c[i][i]>0  and d[i]>0 :
            j=j+1
            if i==n and j==n and a[i][j]>2 and a[i][j]<20 :
                break

        else :
            a = np.random.rand(n,n)*20
            c = np.linalg.inv(a)
            d = np.linalg.solve(a,b) 
            i = 0
            j = 0
            k = k+1
    i=i+1
    j=0
print(a)
print(k)
time_end=time.time()
print('Time cost:',time_end-time_start)
