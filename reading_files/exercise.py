from random import  randint as rnd;
import random;
import string
dummy_record = './members.txt'

copy_to = "./new.txt"





def genFiles(source,dest):
 data = "{:<13}  {:<11}  {:<6}\n"

 with open (source, 'w+') as writefile:
  destination =  open(dest,'w')
  destination.write(data.format('date','name','age'))
  writefile.write(data.format('date','name','age'))

  for  i in range(25):
    name =  ''.join(random.choices(string.ascii_letters,k=5))
    age = rnd(18,34);
    date =  str(rnd(2020,2025))  +"/" + str(rnd(1,12)) + "/"+ str(rnd(1,30))
    writefile.write(data.format(date,name,age))

  writefile.seek(0);

  for line in writefile:
   print(line)
   destination.write(line)
  
 
  
 
  
   
genFiles(dummy_record,copy_to )