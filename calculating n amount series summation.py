def summation():
    x = list()
    a = input("input series with ',':")
    a.replace(",","")
    i = 0
    while i < len(a):
        x.append(int(a[i]))
        i += 2
    print(x)

    increasing_amount = x[1] - x[0]
    number_amount = ((x[-1] - x[0])/increasing_amount) + 1
    mean = (x[0] + x[-1])/2
    result = mean* number_amount
    print(result)


summation()


