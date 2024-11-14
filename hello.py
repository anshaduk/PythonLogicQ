#Ask user for their name
# name = input("What's your name:")

# #Say hello to user
# print("Hello " ,name)

# a = int(input())
# b = int(input())

# c = a+b
# print(c)

# print(*object ,sep=' ',end='\n')
# arr = [1,2,3,4,5]
# print(*arr,sep='-',end='/')

# print("hello \"world\" ")

# name = input("Enter your name:").strip().title()
# first , last = name.split(",")
# print(f"hello {last}")

# print(int(input("Enter 1st number:"))+int(input("Enter 2nd number:")))
# x=999
# y=1
# z=x+y
# print(f"{z:,}")

# def main():
#     name = input("What's your name:")
#     hello(name)

# def hello(to="world"):
#     print("Hello, ",to)

# main()

x  = "muhammad".lower()
arr = ""+x[0]
# y = x[0]
for i in range(1,len(x)):
        if x[i]==x[0]:
            arr = arr+'$'
            
        else:
            arr = arr+x[i]
            
print(arr)


x = "mufeed".lower()
arr = ""  # Initialize the result string
seen = set()  # Use a set to keep track of seen characters

for char in x:
    if char in seen:
        arr += '$'  # Replace with '$' if character has been seen
    else:
        arr += char  # Add character to result
        seen.add(char)  # Mark this character as seen

print(arr)

