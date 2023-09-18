a=str(input('enter a string '))
for i in'aeiou':
    if i in a:
        print(a[::-1])
        break
else:
    print('no vowel')