def fibonacci_number(n):
  first=0
  second=1;
  if n==1:
   return 1 
  elif n==0:
   return 0
  else:
   for i in range(n-1):
     next_entry=first+second;
     first=second
     second=next_entry
   return next_entry  
  


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
