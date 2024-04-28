from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    int_list =  [int(item)  for item in numbers]
    int_list.sort(reverse=True)
    largest =''
    for  i in range(len(int_list)):
        largest+=str(int_list[i])
    

   
    return int(largest)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))


[21,2]



