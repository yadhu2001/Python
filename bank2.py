bank=[]
Account={}
choice='y'
while choice=='y' or choice=='Y':
    dict={
        "Name" :'',
        "Address":'',
        "Age":'',
        "Branch":'',
        "Acc_balance":0
    }
    print('''1.Add new acconunt
         2.view accnt detail
         3.Add Balance
         4.Withdraw
         5.quit   ''')
    select=(input('enter your choice'))
    if select=='1':
        Name=str(input('enter your name'))
        Branch=str(input('branch name'))
        Age=str(input('enter your age'))
        Address=(input('enter your address'))

        dict['Name']=Name
        dict['Address']=Address
        dict['Age']=Age
        dict['Branch']=Branch
        dict['Acc_balance']=0
        bank.append(dict.copy())

    elif select=='2':
        for dict in bank:
         for i,j in dict.items():
            print(i,':',j)

    elif select=='3':
       a=int(input('enter your amount'))
       Acc_balance=dict['Acc_balance']
       bank1=bank.copy()
       for i in bank1:
            i.update({"Acc_balance":Acc_balance+a})
       for dict in bank1:
        for a,b in dict.items():
                print(a,':',b)

    elif select=='4':
        Withdraw_Amount=int(input('enter amount to withdraw'))
        for i in bank1:
            Acc_balance=i['Acc_balance']
            if Acc_balance>0:
                if Acc_balance<Withdraw_Amount:
                    print('in-balance')
                    break
                else:
                    i.update({"Acc_balance":Acc_balance-Withdraw_Amount})
            else:
                    print('insfnt balance')
                    break
            for dict in bank1:
                for x,y in dict.items():
                    print(x,':',y)
    elif select=='5':
        print('exit')
        break
    else:
        print('invalid entry')
        