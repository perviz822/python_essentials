

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








def test():
  #print(diagonalDifference(array))
 #staircase(6)
 staircase2(6)
 pass;





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
 




test()