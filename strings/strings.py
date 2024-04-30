import numpy as np
import math
import string
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

def cone_print(thickness,letter):
    for i in range(math.ceil(thickness/2)):
     print((letter*i).rjust(5) +letter + (letter*i).ljust(5))

def cone_reversed(thickness,letter):
    thickness = math.floor(thickness/2)
    for i in range(thickness+1):
     print((letter*(thickness-i)).rjust(5) +letter + (letter*(thickness-i)).ljust(5))





def rangoli (index):
   alphabet='abcdefghijklmnopqrstuvwxyz'
   for i in range(index,0,-1):
      print(( alphabet[(i-1) :(index-i)]).rjust(index) + alphabet[i-1]   + (alphabet[(i-1) :(index-i)]).ljust(index))

  






#rangoli(10)


l1 = [0,1,2,3,4,5]  

l2 =   l1[4:0:-1]
print(l2)




#cone_print(7,'s')
#cone_reversed(7,'s')
