strs = ["eat","tea","tan","ate","nat","bat"]

anagram = {}
for word in strs:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagram:
        anagram[sorted_word].append(word)
    else:
        anagram[sorted_word]=[word]
print(anagram)