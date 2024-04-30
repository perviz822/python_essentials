


# first implement bubble sort

def compare(a, b):
   
    # Compare numbers based on which combination is bigger
    if a + b > b + a:
        return -1  # 'a' should come before 'b'
    else:
        return 1   # 'b' should come before 'a'

def  largest_number_naive(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if  compare(str(arr[j]),str(arr[i])) == 1:
                arr[j] , arr[i]  = arr[i] ,  arr[j]
    return ''.join([str(item)  for item in arr])   




if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))




# Example usage:








