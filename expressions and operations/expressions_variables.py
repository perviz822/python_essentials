import time


#
def swap_case(s):
    a= " "
    for  i in range(0,len(s)):
        if s[i].islower():
           a+=s[i].upper()
        else:
           a+=s[i].lower()
        
    
    return a
'''s = input()
result = swap_case(s)
print(result)'''

#


def print_full_name(first, last):
 print ("Hello {} {}".format(first,last));


 '''print_full_name("parviz","pirizade")'''


def mutate_string(string, position, character):
    p = position;
    char = character
    string = string[:p]+char+ string[(p+1):]
    return string


start_time = time.time()
a = "asdas"

mutate_string(a,2,"g");
elapsed_time = time.time() - start_time
print(elapsed_time);


