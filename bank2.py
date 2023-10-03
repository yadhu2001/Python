bank=[]
Account={}
choice='y'
while choice=='y' or choice=='Y':
    dict={
        "Name" :'',
        "Address":'',
        "Age":'',
        "Branch":'',
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
        bank.append(dict.copy())
    elif select=='2':
        for dict in bank:
         for i,j in dict.items():
            print(i,':',j)
    elif select=='3':
       
       Acc_balance=int(input('enter your amount'))
       bank1=bank.copy()
       for i in bank1:
            i.update({"Acc_balance":Acc_balance})
       for dict in bank1:
        for a,b in dict.items():
                print(a,':',b)