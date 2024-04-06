

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


  

def test():
 #print(diagonalDifference(array))
 #staircase(6)
 #staircase2(6)
 #plusMinus([1,2,-1,0]);
 print(timeConversion('12:45:54PM'))
 
 pass;
test()