word ='aabcccdeefffab'
count = 1
new_word=''
for i in range(len(word)-1):
    if word[i]==word[i+1]:
        count+=1
    else:
        new_word += str(count)+word[i]
        count = 1
print(new_word+str(count)+word[len(word)-1])
