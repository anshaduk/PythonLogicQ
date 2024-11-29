str = "anshad"
result = []
for char in str:
    if str.count(char)>1 and char not in result:
        result.append(char.upper())
    else:
        result.append(char)
joined_result = ''.join(result)
print(joined_result)