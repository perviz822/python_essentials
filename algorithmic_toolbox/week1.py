

def  max_product(arr:list[int]) ->int :
    max  = float('-inf')
    second_max =  float('-inf')
    for i in range(len(arr)):
        if arr[i] > max:
            second_max=max
            max=arr[i]

    return [max,second_max]   

print(max_product([1,2,3,4,5,6]))
           

            
