bank=[]

Account={}

dict={
        "Name" :'asd',
        "Address":'asd',
        "Age":'asd',
        "Branch":'sad',
        "Acc_balance":0,
        
    }


Acc_number=9827

def add_account():
        global Acc_number
       
        dict['Acc_balance']=0
        dict['Acc_number']=Acc_number
        bank.append(dict.copy())
        Acc_number+=1

def add_balance():
       b=int(input('enter your account number'))
       a=int(input('enter your amount'))

       bank1 =bank.copy()
       acc_no=[]
       for i in bank1:
            acc_no.append(i['Acc_number'])

       if b in acc_no:
            print(b)
       else:
            print('Account number not found')
                        

def withdraw_balance():
        b=int(input('enter your account number'))
        Withdraw_Amount=int(input('enter amount to withdraw'))
        bank1 =bank.copy()
        acc_no=[]
        for i in bank1:
            acc_no.append(i['Acc_number'])
        if b in acc_no:
                    for i in bank1:
                        if i['Acc_number']==b:
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
             
         
        else:
            print('Account number not found')
            




choice='y'
while choice=='y' or choice=='Y':
    
    print('''1.Add new acconunt
         2.view accnt detail
         3.Add Balance
         4.Withdraw
         5.quit   ''')
    select=(input('enter your choice'))
    if select=='1':
        add_account()

    elif select=='2':
        view_account()

    elif select=='3':
       add_balance()

    elif select=='4':
        withdraw_balance()

    elif select=='5':
        exit()
        
    else:
        print('invalid entry')