x,y = (int(a) for a in input().split())
if x>=0 and y>0:
    print("{}@{}".format("."*x, "."*y))
if x>=0 and y==0:
    print("{}".format("."*x))
if x>=0 and y<0:
    print("{}@@@{}".format("."*x, "."*(-y)))
if x<0 and y>=0:
    print("@{}@{}".format("."*y, "."*(-x)))
if x<0 and y<0:
    print("@@{}@{}".format("."*(-x), "."*(-y)))

