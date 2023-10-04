bank=[]

Account={}

# bank1 =bank.copy()
dict={
        "Name" :'',
        "Address":'',
        "Age":'',
        "Branch":'',
        "Acc_balance":500
    }



def add_account():
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



def view_account():
        for dict in bank:
         for i,j in dict.items():
            print(i,':',j)


def add_balance():
     
       a=int(input('enter your amount'))
    #    Acc_balance=dict['Acc_balance']
       bank1 =bank.copy()
       for i in bank1:
            Acc_balance=i['Acc_balance']
            i.update({"Acc_balance":Acc_balance+a})
       for dict in bank1:
        for a,b in dict.items():
                print(a,':',b)

def withdraw_balance():
        Withdraw_Amount=int(input('enter amount to withdraw'))
        bank1 =bank.copy()
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

