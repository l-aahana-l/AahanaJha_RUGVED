def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
term= int(input("Enter the number of terms: "))
series = [fibonacci(i) for i in range(term)]
for num in series:
    print(num, end=" ")
