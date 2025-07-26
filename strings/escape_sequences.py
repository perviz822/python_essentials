import time
#escape sequences

print('I hope everyone is doing okay. \n Are you doing okay ?')
print ('In every programming language the first program you write says \"Hello world\"')\


#string formatting

#1

s1 = 'Thirty'
s2='Days'
s3 ='Of'
s4 = "Python"

conc = s1 + s2 + s3 + s4 

#3
print(conc.upper())
print(conc.lower())

print(conc.title())
print(conc.swapcase())
print(conc.capitalize())


#4
s5 ='Coding For All'

#printing the first word

print(s5[:7])


#4 
print(s5.index('Coding'))
#returnsindex the 
#otherwise returns  a valueerror


#5
print(s5.replace('Coding','Not Cosing'))


print(s5.split(' '))


#6
s6 ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(s6.split(','))
#7
print(s6[0])

#8

s7 ='Python For Everyone'


################### Acronym

start = time.time()
temp_s7 = s7.split(" ")
charc =" "
for s in temp_s7:
    print(s)
    charc = charc + s.capitalize()[0]

end=time.time()    
print("Execution time:"+ format( (end - start),'.10f') +  " " +"seconds")


##################




start = time.time() #Acronym
charc = ''.join(word[0].upper() for word in s7.split(" "))
end=time.time()    

print("Execution time:"+ format( (end - start),'.10f') +  " " +"seconds")

#################


s8 = "Coding For AllC"


print("".join(word[0] for word in s8.split(" ")))


#first occurence

print(s8.index("C"))


#last occurence

print(s8.rindex('C'))

sentence = "You cannot end a sentence with because because because is a conjunction"
#slicing out part of a sentence

print(" ".join(sentence.split()[6:9]))

print(s8.startswith("Coding"))

print(s8.endswith("Coding"))


s9='   Coding For All      '  

#removing white spaces
print(s9.strip())




#formatting

radius = 10
pi = 3.14
area = pi*(radius**2)

print( "The area of the circle with radius of {:.2f} is {:.2f} ".format(radius,area))
print(f"The area of the circle with radius of {radius:.2f} is {area:.2f}")


my_num = 23.2323232

print(format(my_num, ".2f"))

print(f"{my_num:.2f}")