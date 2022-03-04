#Pythagoras triangle pair finder
def tra():
    a = int(input("Input first number:"))
    b = int(input("Input second number:"))
    for i in range(a,b+1):
        for j in range(a,b+1):
            c = ((i ** 2) + (j ** 2)) ** 0.5
            if c == int(c):
                print("{}^2 + {}^2 = {}^2".format(i,j,c))
            else:
                continue

tra()