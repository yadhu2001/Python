range(5)
a=int(input("enter a limit"))
for i in range (1,a+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print('')
for i in range (a,0,-1):
    for j in range(1,i+1):
            print(j,end=' ')
    print('')
        