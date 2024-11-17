def fatorial(number):
    f = 1
    for i in range(1,number+1):
        # f += f*i
        f *=i

    print(f)

fatorial(5)


###using math.factorial###

# import math
# fact = math.factorial(10)
# print(fact)

###using Recursion###

# def fact(num):
#     if num == 0 | num == 1:
#         return 1
#     return num*fact(num-1)

# print(fact(10))

