#Lambdas and list comprehensions



str1 = 'parvizpirizade'

l1 = [i for i in str1]

print(l1)

listOfNumbers =[i for i in range(23)]

listOfEvenNumbers = [i for i in listOfNumbers if i%2==0]

print(listOfNumbers)

print(listOfEvenNumbers)


#lambda functions

myFirstLambdaFunction = lambda a,b:a+b

print(myFirstLambdaFunction(1,2))

selfInvokingLambda =  (lambda a,b:a+b)(12,23) 

print(selfInvokingLambda)

#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negativeAndZero = [i for i in numbers if i  <=0 ]
print(negativeAndZero)

#2 Flatten the following list of lists of lists to a one dimensional list 
nested = [[1, 2], [3, 4], [5, 6]]

nested = [[1, 2], [3, 4], [5, 6]]

flattened = [item for sublist in nested for item in sublist]

nested3 = [   [ [1, 2], [3, 4] ],      [ [5, 6], [7, 8] ]    ]

flattened2=[]

'''

for child1 in nested3:
    for child2 in child1:
        for child3 in child2:
            flattened.append(child3)

'''

flattened2 =  [child3 for child1 in nested3 for child2 in child1 for child3 in child2]

print(flattened2)



        





