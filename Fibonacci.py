print("Fibonacci")
l = int(input("Fibonacci range:"))
a = 1
b = 1
fibonacci = [a,b]
for x in range(l - 2):
    a,b = b,a+b
    fibonacci.append(b)
    print(fibonacci)