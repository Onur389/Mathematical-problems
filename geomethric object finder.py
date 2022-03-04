print("GEOMETHRIC SHAPE FINDER:")
print("*Quadrangle\n*Triangle")
shape = str(input("input shape:"))
if shape == "Quadrangle":
    edge1 = float(input("input edge1 length:"))
    edge2 = float(input("input edge2 length:"))
    edge3 = float(input("input edge3 length:"))
    edge4 = float(input("input edge4 length:"))
    if edge1 == edge2 == edge3 == edge4:
        print("edge1: {}\nedge2: {}\n edge3: {}\nedge4: {}\nSquare".format(edge1,edge2,edge3,edge4))
    elif edge1 == edge2 and edge3 == edge4:
        print("edge1: {}\nedge2: {}\n edge3: {}\nedge4: {}\nRectangle".format(edge1,edge2,edge3,edge4))
    elif edge1 == edge3 and edge2 == edge4:
        print("edge1: {}\nedge2: {}\n edge3: {}\nedge4: {}\nRectangle".format(edge1,edge2,edge3,edge4))
    elif edge1 == edge4 and edge2 == edge3:
        print("edge1: {}\nedge2: {}\n edge3: {}\nedge4: {}\nRectangle".format(edge1,edge2,edge3,edge4))
    else:
        print("edge1: {}\nedge2: {}\nedge3: {}\nedge4: {}\nQuadrangle".format(edge1,edge2,edge3,edge4))
elif shape == "Triangle":
    edge1 = float(input("input edge1 length:"))
    edge2 = float(input("input edge2 length:"))
    edge3 = float(input("input edge3 length:"))
    if not (abs(edge1 - edge2) <= edge3 and edge3 <= abs(edge1 + edge2)):
        print("It's not a Triangle")
    elif not (abs(edge1 - edge3) <= edge2 and edge2 <= abs(edge1 + edge3)):
        print("It's not a Triangle")
    elif not (abs(edge2 - edge3) < edge1 and edge1 <= abs(edge2 + edge3)):
        print("It's not a Triangle")
    elif edge1 == edge2 == edge3:
        print("edge1: {}\nedge2: {}\nedge3: {}\nEquilateral Triangle".format(edge1,edge2,edge3))
    elif edge1 == edge2 != edge3:
        print("edge1: {}\nedge2: {}\nedge3: {}\nIsosceles Triangle".format(edge1,edge2,edge3))
    elif edge1 == edge3 != edge2:
        print("edge1: {}\nedge2: {}\nedge3: {}\nIsosceles Triangle".format(edge1,edge2,edge3))
    elif edge2 == edge3 != edge1:
        print("edge1: {}\nedge2: {}\nedge3: {}\nIsosceles Triangle".format(edge1,edge2,edge3))
    elif edge1 != edge2 != edge3:
        print("edge1: {}\nedge2: {}\nedge3: {}\nTriangle".format(edge1,edge2,edge3))
