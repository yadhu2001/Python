# create a python program to count the number of c's and d's in a string and check them if they are balanced.thatis the total number of c = total number of d, without using in-built function.

# Srting= Do Not Defect Other User Without Permission of concered faculity

a='Do Not Defect Other User Without Permission of concered faculity'
c=0
d=0
for i in a:
    print(i)
    if i=='C' or i=='c':
        c=c+1
    if i=='D' or i=='d':
         d=d+1
if c==d:
    print('both are balanced')
else:
    print('not balanced')

print(c,"is the number of c in string")
print(d,"is the number of d in string")
