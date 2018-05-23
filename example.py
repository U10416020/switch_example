import matplotlib.pyplot as plt
import numpy as np
import math
#x = np.array([[1,0,0,0])
#w = np.array([1,1,-1,0.5])
x = [1,0,0,0]
w = [1,1,-1,0.5]
c = 0.9
w1 = [1,1,-1,0.5]

for i in range(0,200):
  sum = 0
  for j in range(0,4):
    sum += x[j]*w[i*4+j]
    print (str(i) +" "+str(j)+": "+str(sum))
  if sum>=0:
    temp = 1
  else:
    temp=-1
  for k in range(0,4):
    w.append(w[i*4+k]+c*temp*x[k])
  c = c*0.95
  

for i in range(0,200):
  for j in range(0,4):
    sum +=  math.exp(w[i*4+j])
  for j in range(0,4):
    w1.append(math.exp(w[i*4+j])/sum)
    print (w1[i*4+j])
