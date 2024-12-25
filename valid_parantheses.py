string = '({[]})'
def valid(string):
    stack = []
    matching_char = {')':'(',']':'[','}':'{'}
    for char in string:
        if char in matching_char.values():
            stack.append(char)
        elif char in matching_char.keys():
            if stack and stack[-1]==matching_char[char]:
                stack.pop()
            else:
                return False
    return len(stack)==0

print(valid(string))
                
