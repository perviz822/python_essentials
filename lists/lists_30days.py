import math
#adding an item to a list .append()
#inserting an item, will shift  the values to the right
#insert(index,item)
#remove(value)
#pop() will remove the value from the end
#del lst[index]

#list1 = list2 +list3

#extend
#count()



num1 =24


num2 =0


num2=num1
num2 =50

print(num1)




# l1 =[1,2,3,4,5]

# l2=[]

# l2 =l1

# l2[0]=58

# print(l1)


#1
l1 = []

l2 =[1,2,3,4,5]


print(l2[0])
print(l2[len(l2)-1]
)

print(l2[math.floor(len(l2)/2)])

l3 = ['person1','person2','person3','person4']

mid_index =math.floor(len(l3)/2)

l3.insert(mid_index,'person5')


print(l3)
print(mid_index)

#15
print("person6" in l3)


print(l3[:3])

#16 slice out last 3
print(l3[len(l3)-3:len(l3)])


print(l3.pop())



#remove the first item


l4 =['Ulvi','Parviz','Kamil','Cahandar','Zaur']

### removing the first item

#print(l4.pop(1))

print(l4)



mid_index =math.floor(len(l4)/2)

print(l4.pop(mid_index))


#destroying the list

#del l4


#removing all elements

l4.clear()




front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']


full_stack = front_end + back_end


full_stack2 = full_stack.copy()







ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 89]

ages.sort()

max_age = max(ages)
min_age = min(ages)


ages.append(max_age)
ages.append(min_age)


n = len(ages)

if n % 2 == 1:  # odd length
    median = ages[n // 2]




#difference between sort and sorted

#list.sort() returns nothing, it mutates the list
#sorted(list) returns copy of the list sorted, must be assigned to a new variable