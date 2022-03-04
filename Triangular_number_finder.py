def trnufinder():
    a = int(input("input range:"))
    x = list()
    for i in range(a+1):
        for n in range(i-1):
            if i == (n*(n+1))/2:
                x.append(i)
    print("Triangular numbers in range {}:".format(a),x)


trnufinder()