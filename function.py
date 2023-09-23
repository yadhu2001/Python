# Correction required

range(5)
a=int(input("enter a limit"))
for i in range (1,a+1):
    pattern='*'
    for j in range(1,i+1):
        pattern=pattern+str(j)
    print(pattern)
            # print('*',j,end=' ')
    for k in range(i-1,0,-1):
            print(k,end=' ')
    print('*')      
    print('')
b=a-1
for i in range (b,0,-1):
    print('*')
    for j in range(1,i+1):
            print(j,end=' ')
    for k in range(i-1,0,-1):
          print(k,end=' ')
    print('*') 
    print('')
        