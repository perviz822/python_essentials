
import copy


# create  and print list
my_list = [1,2,23]
#print(my_list)


#iterate through  the list



#modify the list element
my_list[2]=78;      

#append an element
my_list.append(56)

#append multiple elements
my_list.extend([1,2,2,3])
#print(my_list)
#interesting note: here we are not adding a list to a list, this [] syntax is  just used to add multiple items

my_list.append([1,2,3,4]) # but this one will add   a list to a list
#print(my_list)


#insert an element
my_list.insert(0,455)
#print(my_list)

#remove  an element
my_list.remove([1,2,3,4])


#remove element by index
del my_list[0]
# does not return a value

#print(my_list)





#deep copy and shallow copy
my_list2 =  my_list.copy()

# for this copy only a new parent reference is created not for the children,the copied  list will still have references to the same children object
my_list3 =  copy.deepcopy(my_list)
# this is a complete copy, with both  new  parent reference and child reference






### demonstrating shallow copy
a = [[1,2,3],[1,2,3]]

b = a[0]
c =a[1]

d =  a.copy()
t = a[0]    
r=a[1]

#print(d is a)
#print(r is c)
#print(r is c)


#reversing
my_list4 =  my_list+my_list2;
print(my_list4)
my_list4.reverse()
print(my_list4)

#remove the duplicate elems 
list5 = [1,2,3,3,3,2,2,2,3]
list5 =  list(set(list5));
#print(list5)




def compareTriplets(a, b):
        scores=[0]*2;
        
        for i in range (0,len(a)):
            if a[i] > b[i]:
             scores[0] +=1;
            elif a[i]<b[i]: 
             scores[1] +=1;
             
        return scores      





l1 = [1,2,3]
l2=[2,3,4]


#print(compareTriplets(l1,l2))



def diagonalDifference(arr):
  ltr_sum=0;
  rtl_sum=0;
  for j in range(0,len(arr)):
    print(a[j][j])
    ltr_sum+=a[j][j];
    
  for  i in range(0,len(arr)):
    rtl_sum +=  arr[i][len(arr)-1-i]#
    
  return abs(rtl_sum-ltr_sum)

array = [[1,2,3],[4,5,6],[7,8,9]]

print(diagonalDifference(array))