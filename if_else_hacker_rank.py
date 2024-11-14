# n = int(input("Enter a number: "))
# if n%2!=0:
#     print("weird")
# elif n%2==0 and n>=2 and n<=5:
#     print("not weird")
# elif n%2==0 and n>=6 and n<=20:
#     print("weird")
# else:
#     print("not weird")

# n = int(input().strip())
# if n%2!=0:
#     print("weird")
# elif n in range(2,5) and n%2==0:
#     print("not weird")
# elif n in range(6,20) and n%2==0:
#     print("weird")
# else:
#     print("not weird")

# n = int(input())
# i=1
# for i in range(i,n+1):
#     print(i)

if __name__ == '__main__':
    n = int(input("Enter your floor: "))
    for i in range(-1,n+1):
        if(i==-1 and i==n):
            print("open in -1th floor")
        elif(i==0 and i==n):
            print("open in 0th floor")
        elif(i==1 and i==n):
            print('open in 1st floor')
        elif(i==2 and i==n):
            print("open in 2nd floor")
        elif(i==3 and i==n):
            print("open in 3rd floor")
        elif(i==4 and i==n):
            print("open in 4th floor")
        elif(i==5 and i==n):
            print("open in 5th floor")
        elif(i>5 and i==n):
            print("please choose other...")