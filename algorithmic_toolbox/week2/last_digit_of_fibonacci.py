
#naive solution
def fibonacci_last_digit_naive(n):
    first = (0, 1)
    if n in first:
     return n
    previous, current = first

    for _ in range(n - 1):
     previous, current = current, previous + current 
	 
    return current%10




#better solution
def fibonacci_last_digit(n):
    first = (0, 1)
    if n in first:
     return n
    previous, current = first

    for _ in range(n - 1):
     previous, current = current, (previous + current) % 10
	 
    return current
 