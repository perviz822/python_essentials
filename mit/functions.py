
x=6
l = [1,2,3]

def change_value(x):
    x=8
    l.append(89)
    
    
    
print(x)

change_value(x)

print(x)   
print(l) 
    
#since integer is immutable and its value can not be changed, the x inside the function is treated as  new variable belonging to the function env.
    
    
    
# functions are first class object
    