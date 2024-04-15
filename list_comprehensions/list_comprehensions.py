import numpy as np 
import math

l1 = [1,12,3,4,5]

l2 = [item**2 for item in l1]

print(l2)

l3 = [int(math.sqrt(item))  for item in l2]

print(l3)

l4 =  [item for item in l3 if item>10]


l5=  [item for item in l4 if item <4]