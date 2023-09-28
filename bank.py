Account={}
N=input("enter your name")
A=input("enter yopur address")
Ag=input("enter your age")
C=input("enter your contact number")

print("Account details")
Account['Name']=N
Account['Address']=A
Account['Age']=Ag
Account['Contact']=C
for i,j in Account.items():
    print(i, ':', j)
