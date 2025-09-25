def Divide(string, n):
    length = len(string)
    if length % n != 0:
        print("String length is not divisible by n")
        return
    part = string[:n]
    for i in range(0, length, n):
        if string[i:i+n] != part:
            print("Parts are not same")
            return
    parts = [string[i:i+n] for i in range(0, length, n)]
    print(", ".join(p for p in parts))
string = input("Enter the String:")
n = int(input("Enter the number:"))
Divide(string, n)
