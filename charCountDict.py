from collections import Counter

str = "hello"
char_count = Counter(str)
dict_char_count = dict(char_count)
print(dict_char_count)

# str= "hello"
# char_count = {}
# for char in str:
#     char_count[char] = char_count.get(char,0)+1
# print(char_count)