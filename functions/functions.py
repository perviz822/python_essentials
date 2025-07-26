import numpy as np


print("i am change5")

#change5

# achange from  branch1


#arbitrary number of arguments

def first_func(*args):
    print(type(args)) #tuple
    sum =0 
    for  arg in args :
        sum+=arg;

    return arg


print(first_func(1,2,3,4,5))



#functions return None, when there is no return defined




b =15
def f1(b):
  b=78
  pass;


def func1 (b):
   b=36
   f1(b)
   print(b)
   pass;

func1(b)

print(b)



