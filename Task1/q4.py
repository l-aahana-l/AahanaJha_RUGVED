def selectionSort(s):
    chars = list(s)
    n = len(chars)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if chars[j] < chars[min_idx]:
                min_idx = j
        chars[i], chars[min_idx] = chars[min_idx], chars[i]
    return ''.join(chars)
inputstr = input("Input String: ")
sorted_str = selectionSort(inputstr)
print("Sorted String:",sorted_str)
