
a=["flower","flow","floght"]
c=len(min(a))
# print(c)
d=''

for i in range(c):
    b=a[0][i]
    # print(b)
    for j in a[1:]:
        # print(j)
        if j[i]!=b:
            print(d)
            exit()
    d+=b




















# for i in range(0,c):
#     b=a[2]
#     for j in a[1]:
#         # print(j[i])
#         print(b[i])
#         # if j[i]!=b[i]:
#         #      break
#         # else:
#         #      print(j[i])
#         # break

      






    #     # print(i,j)
    #     if i==j:
    #         print(i)
    # #    if i!=j:
    # #     break
    # #    else:
    # #     print(i,j)
                