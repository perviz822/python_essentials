import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,4])

#print(type(a))

#a.size

#a.ndim  rank of the array

#a.shape

''''
a[0] = 12;
c = a[0:4];
print(c)
'''

#vector addition

u= np.array([[0],[1]])
v = np.array([[2],[1]])


'''print(np.dot(u.T,v))

print(u-v)

print(u+v) #element wise addidition

'''
#mapping


x =  np.array([0,np.pi/2,np.pi])  

y=np.sin(x)   #universal function

#np.linspace


x = np.linspace(0,1 ,10)

y =np.sin(x)


plt.plot(x,y)

#a comment deleted

d =  np.array([[1,2,3],
               [3,4,5],
               [2,2,3]])

e=  np.array([[1,2,3],
               [3,4,5],
               [2,2,3]])
#print(d.ndim)


#print(d.shape)

print(d[2:3,1:3]) # slicing 2d arrays
print(d+e)

print(e);