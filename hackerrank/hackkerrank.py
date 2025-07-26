import re
import time
import timeit
from collections import OrderedDict

def diagonalDifference(arr):
  ltr_sum=0;
  rtl_sum=0;
  for j in range(0,len(arr)):
    print(arr[j][j])
    ltr_sum+=arr[j][j];
  print(ltr_sum)
  for  i in range(0,len(arr)):
    rtl_sum +=  arr[i][len(arr)-1-i]#
  print(rtl_sum)  
  return abs(rtl_sum-ltr_sum)




def staircase(n):
    # Write your code here
    #scale=[]
    for i in range(n):
        text=''
        for _ in range(n-i):
            text+=" "
        for _ in range(i+1):
            text+="#"
        #scale.append(text)
        print(text)




def staircase2(n):
    for i in range(1,n+1):
        print(" "*(n-i) + "#" *i)        
 









def plusMinus(arr):
    count_pos=0
    count_negative =0;
    count_zero=0;
    size = len(arr);
    for i  in range(len(arr)):
        if  arr[i] >0 :
            count_pos +=1;
        if arr[i]==0:
            count_zero +=1;  
        if arr[i] <0:
            count_negative+=1;
   
    print(round(count_pos/size,6))
    print(round(count_negative/size,6))
    print(round(count_zero/size,6))
        
          



def add_zero_if_nec(s):
    
    if s[0]=='0':
      return int(s[1])
    elif s[0:2]=='12':
      print(' itis12')
      return 0
    
    else:
     return int(s[0:2])  
    
      
  
    

def timeConversion(s):
 
  my_list  = s.split(":")
  print(my_list[0])
  ending= my_list[len(my_list)-1][2:]
  print(ending)
  my_list[len(my_list)-1] = my_list[len(my_list)-1][0:2]
  
  if ending=='PM':
    print('ending is pm')
    my_list[0]=str(add_zero_if_nec(my_list[0])+12)

  else:
     if my_list [0]=='12':
        my_list[0]='00'  
   
   
  return ':'.join(my_list) 


  
def gradingStudents(grades):
    grades_list =[]
    for i in range(len(grades)):
        j=1;
        divisible_by_5=0;
        if grades[i] < 40:
           grades_list.append(grades[i])
        else:   
          while ((grades[i]+j)%5!=0):
            j+=1
          divisible_by_5 = grades[i]+j
          if  divisible_by_5 - grades[i]<3:
            grades_list.append(divisible_by_5)
           
           
          else:
            grades_list.append(grades[i])   

    return grades_list     
                


'''def gradingStudents(grades):
    updated_grades = []  # Create a new list to store the updated grades
    for grade in grades:
        if grade < 40:
            updated_grades.append(grade)  # Keep grades below 40 unchanged
        else:
            next_multiple_of_5 = (grade // 5 + 1) * 5  # Find the next multiple of 5
            if next_multiple_of_5 - grade < 3:  # Check if rounding up is needed
                updated_grades.append(next_multiple_of_5)  # Round up to the next multiple of 5
            else:
                updated_grades.append(grade)  # Keep the grade unchanged
    return updated_grades'''


def write(string, n):
    i=0
    while i<len(string):
       for j in range(n):
          if i+j >=len(string):
             break
          print(string[i+j], end ='')
       i=i+j+1
       print('\n')   

def print_door_mat ():
 
 args = [int(item) for  item in input("enter the doormat  height and width: ").split(" ")  if item  ]

 t=1

 for i in range(args[0]):
        print('-'* int((args[1]-t*3)//2) , end ='')
        if i !=int((args[0]-1)//2):
          print('.|.'*t, end='')
        else:
            print('-'* int((args[1]-7)//2) , end ='')
            print('WELCOME', end='')  
            print('-'* int((args[1]-7)//2) , end ='')
        print(('-')*(int((args[1]-t*3)//2)) , end ='')

        print()  

        t=t+2 if i !=int((args[0]-1)//2) and i<int((args[0]-1)//2) else t-2
    
   




'''

# here in this task we make sure that each value  takes the same amount space as the longest string
# for example   : rjust
1 2 3              -->    1    2    3
1234 3455 3454         1234 3455 3454

ljust
1 2 3              --> 1    2    3
1234 3455 3454         1234 3455 3454

'''
def print_formatted(n):
  max_space =  len(bin(n))-2
  for i in range(1,n+1):
   octal =format(i,'o')
   binary  = format(i,'b')
   hexa =  format(i,'X')
   print("{i} {octal} {hexa} {binary}".format(i=str(i).rjust(max_space) ,octal=octal.rjust(max_space),binary=binary.rjust(max_space),hexa=hexa.rjust(max_space)))

   
def print_second_max (arr):
    l = list(arr)
    l= [item  for item in l if item != max(l)]
    print(max(l))

'''

The provided code stub will read in a dictionary containing 
key/value pairs of name:[marks] for a list of students. Print
the average of the marks array for the student name provided, 
showing 2 places after the decimal.
'''


def print_average_marks():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()    
    print(student_marks.values())
    sum=0
    for  elem in student_marks[query_name]:
        sum+=elem
  
    print("{:.2f}".format(sum/len(student_marks[query_name])))
    
    
    
def capitalize_full_name(s):
   result = []
   words = s.split()
   for word in words:
     capitalized_word = word[0].upper() + word[1:]
     result.append(capitalized_word)
     
   return ' '.join(result)  
 
def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

  

def get_all_substrings(s):
    player1 = {'name':'Stuart','score':0}
    player2 = {'name':'Kevin','score':0}
  
    vowels = ['a', 'e', 'i', 'o', 'u']
    length = len(s)
    vowel_words = set([s[i:j] for i in range(length) for j in range(i + 1, length + 1) if s[i:j][0].lower() in vowels])
    consonant_words = set([s[i:j] for i in range(length) for j in range(i + 1, length + 1) if s[i:j][0].lower() not in vowels])
    
    for substr in vowel_words:
      player2['score']+= occurrences(s,substr)
      print(substr,s.count(substr))
    for substr in consonant_words:
      player1['score']+=occurrences(s,substr)
      
    print(vowel_words)
    print(consonant_words)  
     
    if player1['score'] ==player2['score']:
      print('Draw')
    else:
      winner =  max(player1, player2, key=lambda player: player['score'])   
      print (winner['name'] + ' ' + str(winner['score']))
  
  
def find_string(substr, string):
  return string.find(substr)


def replace_string(sentence, old_word, new_word):
  return sentence.replace(old_word,new_word)



def customized_replace(string,start,end,new_word):
  return string.replace(string[start:end],new_word)
  
  
print(customized_replace('banana',1,4,'ata')  )


def  upper_vowels(string):
  vowels = 'aeiou'
  
  for vowel in vowels:
    string = string.replace(vowel,vowel.upper())
    
    

"""

Task 1: Find All Occurrences of a Substring
Write a function that finds all occurrences of a substring in a string and returns a list of the starting indices of each occurrence. 
You can use the find() method in a loop to achieve this.

"""

def merge_the_tools(string, k):
    substrings = []
    
    for i in range(0, len(string), k):
        sub = string[i:k+i]
        unique_chars = []
        for j in sub:
            if j not in unique_chars:
                unique_chars.append(j)
        substrings.append(''.join(unique_chars))
        
    for str in substrings:
        print(str.upper())   
        
        
        
        
        
        


   
   

    
  
  
  
  
 
  

  
      
    



         
   



   

  
def test():
 #print(diagonalDifference(array))
 #staircase(6)
 #staircase2(6)
 #plusMinus([1,2,-1,0]);
 #print(timeConversion('12:45:54PM'))
 #print(gradingStudents([29,23,45,49,18]))  
 #write('asdadfsdfsd',4)
 #print_formatted(12)
 #print_second_max([6,6,622,34,31,2,3])
 #print_average_marks()
 #print( get_all_substrings('BANAASA'))
 
 #print( merge_the_tools('bananasaaasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdawdqweqwdasdasdasdasdasd',3)  )  
 print(capitalize_full_name("hello world lol")
 )
 
 pass;
test()


# a new change



#find
#replace
#count
#upper
#lower
#strip
#slice
#upper
