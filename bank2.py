bank=[]
for i in range(1):
    dict={
        "name" :'',
        "branch":'',
    }
    name=str(input('enter your name'))
    branch=str(input('branch name'))
    dict['name']=name
    dict['branch']=branch
    bank.append(dict)
    for j in bank:

        print(j)    