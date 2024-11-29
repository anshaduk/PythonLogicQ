def most_common_ele(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] = frequency[num]+1
        else:
            frequency[num] = 1

    max_freq = max(frequency.values())
    candid = [key for key,value in frequency.items() if value == max_freq]
    return min(candid)

print(most_common_ele([1, 2, 3, 2, 1, 4, 1]))
