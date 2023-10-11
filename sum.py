# def two_sum(nums, target):
#     num_indices = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_indices:
#             return [num_indices[complement], i]
#         num_indices[num] = i
#     return []
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# print(result)

list3=[]
list=[1,2,3,4,5,6]
for i in range(len(list)):
        for j in range(len(list)):
            target=9
            list2=[]
            if list[i]+list[j]==target:
                list2.append(list[i])
                list2.append(list[j])
                list3.append(list2)
for k in list3:
     print(k)
# print(list3)
            
        
