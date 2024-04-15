
#()
#tuples are ordered sequences
#tuple can contain any type
#can be acessed with index
#negative index can be used
# we can add two tuples, it will merge them we can concatanate them
# we can slice tuples
#len of  tuples
# they are immutable
# we can have nested tuples
# can be accessed by classic way




#lists
#ordered sequence
# []

#  lists are mutable
#  can have multiple data types
#  can be accessed via index
#  we can perform slicing in list
#  they can be merged with + operand
#  extend  method can add  multiple elements
#  append method only adds one element
#  we can modify  the element by it's index
#  del method
#  split method


#n = int(input())
#integer_list = map(int, input().split())
#print(integer_list)


# A tuple of integers
#my_tuple = (1, 2, 3)

# Calculate and print the hash value of the tuple
#print(hash(my_tuple))   

# using  tuoples as keys
my_dict = {
    (12,11):"parviz",
    (23,43):"cavid",
    (21,234):"xamraz",
    (23,54):"Sedaqet"
}

#tuples can be used as keys, because they are immutable, and hashable
#print(my_dict.keys())

days = ('monday','tuesday',"wednesday","thursday","friday","saturday","sunday")

# access the  entries
#print(days[0])
#print(days[len(days)-1])

# tuple slicing
weekdays =  days[0:5];
#print(weekdays)

a_day_tuple =days[0:1]
#print(a_day_tuple)

empty_tuple = ();

#print(type(empty_tuple))

weekends= (days[len(days)-3:len(days)-1])

get_week_back =  weekdays+ weekends
#print(get_week_back)


my_str =  ",".join(get_week_back)
string_tuple_1 = tuple(my_str.split(","))
string_tuple_2 = tuple(my_str)
#print(string_tuple_1)
#print(string_tuple_2)



#print("monday" in string_tuple_1)




#packing
#unpacking
mixed_tuple = (23,"Parviz","Pirizade",{"math":90,"physics":45})
age, name, surname, grades = mixed_tuple;

def return_tuple(*args):
    my_tuple = tuple(args)
    print(my_tuple)
    return my_tuple;


returned_tuple =  return_tuple('a','b','v')
print(type(returned_tuple))

###

#list = [("parviz",82),("cavid",94),("sadagat",65)]


###

list_1 = [11,12,23]
list_2 = [11,45,56]
list_3 =  zip(list_1,list_2)

new_list = list(list_3)
print(new_list)

###



###
tuple_1 = (1,3,5,7)
tuple_2 = (2,4,6,8)
tuple_e  = ();


for  i in range(0,len(tuple_1)):
    tuple_e+=tuple_1[i:i+1] +tuple_2[i:i+1]



print(tuple_e)

###




nested_tuple = (weekdays,weekends);


def  return_multiple():
    age = 20;
    name = "john"
    country="USA"
    return age, name, country




age,name,country = return_multiple()
print(type((age,name,country)))








