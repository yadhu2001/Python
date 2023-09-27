
choice='y'
a=[]
while choice !='n':
    print('''
         To-Do List'''
        '''
          1)Add more data
          2)Remove data
          3)view my schedule
          4)exit the list   ''')
    select=int(input('choose a number'))
    if select==1:
        b=str(input('enter a string'))
        a.append(b)
    elif select==2:
        b=str(input('selct the element you want to remove'))
        a.remove(b)
    elif select==3:
        for i in a:
            print("*",i)
    elif select==4:
        print('quiting the list')
        break
    else:
        print('invalid entry')
        
        

    

