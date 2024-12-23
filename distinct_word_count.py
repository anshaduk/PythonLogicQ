from collections import Counter

n = int(input())
word  = [input() for _ in range(n)]
word_count = Counter(word)
print(len(word_count))
print(*word_count.values())
