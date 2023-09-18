a=input('enter a string')
z=0
for i in 'aeiou':
    # print(i)
    if i in a:
        # print('vowel found') 
        z=z+1
if z>0:
    print(z)
else:
    print('vowel not found')