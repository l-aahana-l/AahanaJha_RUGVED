def first_repeating(arr):
    seen = set()
    first_repeat_index = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] in seen:
            first_repeat_index = i
        else:
            seen.add(arr[i])
    if first_repeat_index != -1:
        print("First repeating element is", arr[first_repeat_index],"at index",first_repeat_index)
    else:
        print("No repeating element found!")
arr = []
num=int(input("Enter number of element:"))
print("Enter elements:")
for i in range(num):
    element=int(input())
    arr.append(element)
first_repeating(arr)
