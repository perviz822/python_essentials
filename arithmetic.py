import math


def  mix_of_float_int(num1, num2):
    return type(num1+num2) # type float, because integer is narrower than  float




def  division(num1,num2):
  res1 = num1/num2
  res2 = num1//num2 # rounds down to nearest integer

  print("type:" + str(type(res1)), "value:"+ str(res1))
  print("type:" + str(type(res2)), "value:"+ str(res2))




def simple_arithmetic(a,b):
   sum = a + b 
   diff = a-b
   quotient = a/b
   remainder = a%b
   return {'sum' :sum,'diff':diff,'quotient':quotient,'remainder':remainder}



def converter(num):
    if isinstance(num,int):
     return float(num)
    elif isinstance(num,float):
     return int(num)




def power(num):
   pow2 = pow(num,2)
   pow3 =pow(num,3)
   pow4= pow(num,4)
   pass;
#division(15,3)




def min_change(payed , cost,denoms):
    assert isinstance(payed,int), "payed amount should be an integer"
    assert isinstance(cost,int),  "cost amount should be an integer"
    change = payed - cost
    denoms = sorted(denoms,reverse =True)
    min_num =0
    for val in denoms:
       count = change//val
       print(count)
       min_num +=count
       change = change%val

    return min_num   

def min_change_handles_floor(payed , cost,denoms):
    change = round(payed - cost,2)
    denoms = sorted(denoms,reverse =True)
    min_num =0
    for val in denoms:
       count = change//val #float // int = float
       min_num += count
       change = change%val

    return min_num   

print(min_change_handles_floor(200,120.5,[50,20,10,5,2,1]))
      


   


