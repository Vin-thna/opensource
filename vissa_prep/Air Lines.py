import math
def f(x,n):
    cc=x*100
    res=n-cc
    return math.ceil(res/100)
x,n=map(int,input().split())
print(f(x,n))
