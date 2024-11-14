import getpass

print(getpass.getuser()) # get current username

password = getpass.getpass("Enter your password:")
print("You entered : ",password)
