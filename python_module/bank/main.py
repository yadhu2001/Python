from master import *

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
        