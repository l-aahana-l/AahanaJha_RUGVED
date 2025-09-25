def credit(number):
    digits = [int(d) for d in str(number)]
    digits.reverse()
    sum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            double = digit * 2
            if double > 9:
                double -= 9
            sum += double
        else:
            sum += digit
    return sum % 10 == 0
creditnum=int(input("Enter the credit card No.:"))
print("Valid number" if credit(creditnum) else "Invalid number")
