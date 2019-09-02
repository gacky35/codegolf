b,n = (int(a) for a in input().split())
x = int(b**(1.0/n))
if b-x**n > (x+1)**n-b:
    a=1+x
else:
    a=x
print(a)
