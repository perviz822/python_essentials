class Point :
   # there is no constructor overload in python, but you can achieve this  like this:
   
    def __init__(self,x=0,y=0):
        self.x= x
        self.y=y
    # every method in python  requires   at least a self argument - main difference between methods and  functions    
    def reset(self):
        self.x=0;
        self.y=0;
        pass    
        
     





p1 = Point()
p2= Point()

# we can dynamically add attributes to  instances
p1.x = 5
p1.y = 4;

# we can also dynamically add attributes to a class

print(p1.x,p1.y)







    



