def isHillNum(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    if length < 3:
        return False
    i = 1
    while i < length and digits[i] > digits[i - 1]:
        i += 1
    if i == 1 or i == length:
        return False
    while i < length and digits[i] < digits[i - 1]:
        i += 1

    return i == length
num = int(input("Enter a number: "))
if isHillNum(num):
    print("Hill number")
else:
    print("Not a hill number")
