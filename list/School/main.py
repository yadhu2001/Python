from master import *

choice='y'
while choice=='y' or choice=='Y':
    
    print('''
          1.Add student
          2.view student
          3.view teachers
          4.add teacher''')
    
    select=(input('enter your choice'))
    if select=='1':
        add_student()

    elif select=='2':
        view_student()
    
    elif select=='3':
        view_teacher()

    elif select=='4':
        add_teacher()
