args = [int(item) for  item in input("enter it").split(" ")  if item  ]

t=1

for i in range(args[0]):
      print('-'* int((args[1]-t*3)//2) , end ='')
     
      if i !=int((args[0]-1)//2):
        print('.|.'*t, end='')
      else:
          print('-'* int((args[1]-7)//2) , end ='')
          print('WELCOME', end='')  
          print('-'* int((args[1]-7)//2) , end ='')
      print(('-')*(int((args[1]-t*3)//2)) , end ='')

      print('\n')  

      t=t+2 if i !=int((args[0]-1)//2) and i<int((args[0]-1)//2) else t-2
      print(t)
    