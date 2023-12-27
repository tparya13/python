def fact(n):
    if n==3:
        return 100
    else:
        return n*fact(n-1)
res=fact(5)
print(res)    