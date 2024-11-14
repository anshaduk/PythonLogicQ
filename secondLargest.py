
l1 = [1,15,3,4,7,10]

for i in range(len(l1)):
    for j in range(0,len(l1)-i-1):
        if l1[j] > l1[j+1]:
            l1[j],l1[j+1] = l1[j+1],l1[j]
print(l1[::-1][1])


# l1 = [1,15,3,4,7,10]
# sortedlist = sorted(l1) 
# sorted_length = len(sortedlist)
# print(sorted_length)
# secondLargest = sortedlist[::-1]
# print(secondLargest[1])

# a=10
# b=20

# print("Before Swaping : ",a,b)
# # a,b = b,a
# # temp = a
# # a = b
# # b=temp

# a=a+b
# b = a-b
# a = a-b
# print("After Swapping : ",a,b)
