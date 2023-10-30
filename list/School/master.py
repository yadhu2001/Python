Std=[]
Teachers=['sam','anirudh','yuvan','shyam']
Account={}
dict={
        "Name" :'',
        "Address":'',
        "Age":'',
        "Class":''
    }
def add_student():
        Name=str(input('enter your name'))
        Address=(input('enter your address'))
        Age=str(input('enter your age'))
        Clas=int(input('enter your class'))
        

        dict['Name']=Name
        dict['Address']=Address
        dict['Age']=Age
        dict['Class']=Clas
        Std.append(dict.copy())

def view_student():
        for dict in Std:
            for i,j in dict.items():
                print(i,':',j)
def view_teacher():
     for i in Teachers:
           print(i)
    
def add_teacher():
    b=int(input('enter your S.number of teacher'))
    a=b-1
    x=int(input('enter the classs'))
    
    for i in Std:
    #  for i in dict:
          if i[Clas]==x:
               print(i)
          i[Teachers]=a
          
        

