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
        Class=int(input('enter your class'))
        

        dict['Name']=Name
        dict['Address']=Address
        dict['Age']=Age
        dict['Class']=Class
        Std.append(dict.copy())

def view_student():
        for dict in Std:
            for i,j in dict.items():
                print(i,':',j)
def view_teacher():
     for i in Teachers:
           print(i)
    
def add_teacher():
      b=input('enter teacher name')
      Std1=Std.copy()
      if b in Teachers:
            for dict in Std:
                  dict['teacher']=b
            Standred=[]
            for i in Std1:
                Standred.append(i['Class'])
            if b in Standred:
             for i in Std1:
                 if i['Teacher']==b:
                  teacher=i['teacher']
                  i.update({"teacher":teacher})
            else:
             print('not found')

        

