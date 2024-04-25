'''
n =  int(input('enter the the number of rows:'))

for i in range (n):
    s =  str(input('enter the string')).split(' ')
    print (s)

'''

a = ['1','2','2','2','3']

myset =  set([int(item) for item in a])
print(myset)
print(sum(myset))