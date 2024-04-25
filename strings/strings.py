import numpy as np
def count_letters(s):
 print("Enter the string")

 vowels = ['a','e','i','o','u'];
 count_v=0;
 count_c = 0;
 for char in s:
    if char.lower() in vowels:
        count_v+=1;
    else:
        count_c+=1;

 print("count of vowels :", end=" ")
 print(count_v)
 print("count of consonants :", end=" ")
 print(count_c)


def look_for_sub_string(s,sub_s):
   contains=False
   for  i in range(0,len(s)):
      if len(s[i:len(sub_s)+i])<len(sub_s):
             break;  
      print(s[i:len(sub_s)+i])
      if s[i:len(sub_s)+i]==sub_s:
         contains=True; 
   return contains  

#print(look_for_sub_string("Azerbaijan","an"))

print('h'.center(8))

for i in range(1,8):
  
    print((('h'*i).rjust(8)),end='')
    print((('h'*i).ljust(8)))
    





      
   
