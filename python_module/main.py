import arith
select=0
while select!=5:
    print(''' 
      1.addition
      2.subtraction
      3.division
      4.multiplication
      5.power
      6.factorial
      7.quit ''')

    select=int(input('enter your choice'))
    if select==1:
        arith.addition()
        
    elif select==2:
        arith.subtraction()

    elif select==3:
        arith.division()

    elif select==4:
        arith.multiplication()

    elif select==5:
        arith.power()

    elif select==6:
        arith.fact()
        
    elif select==7:
        break
    else:
        print('invalid entry')
        break
