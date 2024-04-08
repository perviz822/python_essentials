import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product




def  max_product(arr:list[int]) ->int :
   new_arr= [];
   max  = float('-inf')
   second_max =  float('-inf')
   found=False
   if len(arr) >= 2: 
    for i in range(len(arr)):
        if arr[i] > max:
            second_max=max
            max=arr[i]

    for i in range(len(arr)) :   
        if arr[i]==max  and found==False:
            found=True
            continue
        else:
            new_arr.append(arr[i])    
    for i in range (len(new_arr)):
        if new_arr[i] >second_max:
            second_max=new_arr[i]
    
    return max*second_max  
   else:
       return 0;    
#print(max_product([84,84,38]))



def generate_random_lists(num_lists, min_length, max_length, min_value, max_value):
    lists = []
    for _ in range(num_lists):
        length = random.randint(min_length, max_length)
        # Generate a list of random integers, where the number of integers is 'length'
        rand_list = [random.randint(min_value, max_value) for _ in range(length)]
        if  max_pairwise_product(rand_list) == max_product(rand_list):
            pass;
        else:
            print('results differed in this  input: {}'.format(rand_list))    

    return lists





   

#enerate_random_lists(1000000,0,100,0,100)



def fibonacci(n):
   
    if n <=1:
        return n
    else:
        return  fibonacci(n-1)+ fibonacci(n-2)
    




print(fibonacci(4))

            
