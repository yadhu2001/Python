def addition():
    a=int(input('enter first num'))
    b=int(input('enter second number'))
    print('sum =',a+b)

def subtraction(a,b):
    a=int(input('enter first num'))
    b=int(input('enter second number'))
    print('difference =',a-b)
    
def multiplication():
    a=int(input('enter first num'))
    b=int(input('enter second number'))
    print('product =',a*b)

def division():
    a=int(input('enter first num'))
    b=int(input('enter second number'))
    print('Quo =',a/b)

def power():
    a=int(input('enter first num'))
    b=int(input('enter second number'))
    print('power =',a**b)

def fact():
   num=int(input('enter a number'))
   fact=1
   
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial is",fact)