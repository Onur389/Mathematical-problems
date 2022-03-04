n = input("Input Number")
digit_number = len(n)
digit_value = 0
result = 0
n = int(n)
f = n
while f > 0:
    digit_value = f % 10
    result += digit_value**digit_number
    f //= 10
if result == n:
    print("{} is an armstrong number".format(n))
elif result != n:
    print("{} is not an armstrong number".format(n))