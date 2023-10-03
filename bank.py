
while True:
    print('''1.Add new acconunt
         2.view accont detail
         3.quit   ''')
    choice=int(input('enter your choice'))
    if choice==1:
            Account={}
            N=input("enter your name")
            A=input("enter yopur address")
            Ag=(input("enter your age"))
            C=(input("enter your contact number"))
            print()
            
    elif choice==2:
            print("Account details")
            Account['Name']=N
            Account['Address']=A
            Account['Age']=Ag
            Account['Contact']=C
            for i,j in Account.items():
                print(i, ':', j)
    elif choice==3:
            print('exiting')
            break
    else:
        print('invalid entry')
