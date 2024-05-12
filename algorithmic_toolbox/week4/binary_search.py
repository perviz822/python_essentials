def binary_search (arr,low,high,elem):
  mid_index = (low +high)//2
  if high >=low:
    if arr[mid_index] == elem:
     return mid_index
    elif elem > arr[mid_index]:
         return binary_search(arr,mid_index+1,high,elem)
    elif  elem <arr [mid_index]:
         return binary_search(arr,low,mid_index-1,elem)  
  else:
     return -1;

arr =  [1,2,3,4,56]
print(binary_search(arr,0,len(arr)-1,56))


