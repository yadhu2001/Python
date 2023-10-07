# Account={}
# bank=[]
# dict={}
# # Acc_number=23659
# def kk(Acc_number):
#     a=input("enter your name")
#     dict['name']=a
#     dict['Acc_balance']=0
#     dict['Acc_numer']=Acc_number
#     bank.append(dict.copy())
#     Acc_number+=1
#     print(Acc_number)
#     return Acc_number
# while True:
#     kk(Acc_number)
   
#     print(bank)




def accno(acc):
    acc += 1
    return acc

acc = 0

while acc < 10:
    # a=input("enter your name")
    test=accno(acc)
    print(test)
    