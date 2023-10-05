Account={}
bank=[]
dict={}
Acc_number=23659
while True:
    a=input("enter your name")
    dict['name']=a
    dict['Acc_balance']=0
    dict['Acc_numer']=Acc_number
    bank.append(dict.copy())
    Acc_number+=1
    print(bank)