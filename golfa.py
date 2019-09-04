x,y = (int(a) for a in input().split())
if x>=0:
    print("{}".format("."*x), end='')
    if y != 0:
        print("@{}".format("."*y)) if y>0 else print("@@@{}".format("."*(-y)))
if x<0 and y>=0:
    print("@{}@{}".format("."*y, "."*(-x)))
if x<0 and y<0:
    print("@@{}@{}".format("."*(-x), "."*(-y)))

