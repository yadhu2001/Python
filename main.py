a=5
for i in range (1,a+1):
    pattern='*'
    for j in range(1,i+1):
        pattern=pattern+str(j)
    # print(pattern)
    for k in range(i-1,0,-1):
        pattern=pattern+str(k)
    print(pattern)
    