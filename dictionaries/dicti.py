

d1 = {};

#d1.update({'name':'parviz'})


print(d1)

list_1 = ['parviz','pirizade',23]
list_2 =['name','surname','age']



for  i in range(0,len(list_1)):
    d1.update({list_2[i]:list_1[i]})
#rint(d1)

d2={}

lis_3 = [1,2,3,3,4,1,2,3,12,4,5,6,6,4,3,1,3,3,4,5,67,78,34,5,5];


for  i in  range(0,len(lis_3)):
  d2.update({lis_3[i]:0 })
    
for i in range(0,len(lis_3)):
  if d2[lis_3[i]]==0:
     d2[lis_3[i]]=1;
  else:
     d2[lis_3[i]]+=1

print(d2)     