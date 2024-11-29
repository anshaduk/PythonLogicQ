from collections import Counter

str = "hello"
char_count = Counter(str)
dict_char_count = dict(char_count)
print(dict_char_count)