bank=[]
Account={}
dict={
        "Name" :'',
        "Address":'',
        "Age":'',
        "Branch":'',
        "Acc_balance":0,
        
    }

Acc_number=9827

def add_account():
        global Acc_number
        Name=str(input('enter your name'))
        Branch=str(input('branch name'))
        Age=str(input('enter your age'))
        Address=(input('enter your address'))
        

        dict['Name']=Name
        dict['Address']=Address
        dict['Age']=Age 
        dict['Branch']=Branch
        dict['Acc_balance']=0
        dict['Acc_number']=Acc_number
        bank.append(dict.copy())
        Acc_number+=1
        # print(Acc_number)
       


def view_account():
        for dict in bank:
            for i,j in dict.items():
                print(i,':',j)


def add_balance():
       b=int(input('enter your account number'))
       a=int(input('enter your amount'))
       bank1 =bank.copy()
       acc_no=[]
       for i in bank1:
            acc_no.append(i['Acc_number'])
       if b in acc_no:
            for i in bank1:
                 if i['Acc_number']==b:
                  Acc_balance=i['Acc_balance']
                  i.update({"Acc_balance":Acc_balance+a})
       else:
            print('Account number not found')


def withdraw_balance():
        b=int(input('enter your account number'))
        
        bank1 =bank.copy()
        acc_no=[]
        for i in bank1:
            acc_no.append(i['Acc_number'])
        if b in acc_no:
         Withdraw_Amount=int(input('enter amount to withdraw'))
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
            # for dict in bank1:
            #     for x,y in dict.items():
            #         print(x,':',y)

