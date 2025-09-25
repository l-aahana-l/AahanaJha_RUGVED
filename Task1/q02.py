input_string = input("Input the String: ")
sorted_string = "".join(sorted(input_string))
print("Sorted String:",sorted_string)
count = {}
for char in sorted_string:
    count[char]=count.get(char,0)+1
print("Character count:")
for char in sorted(count):
    print(char,":",count[char])
