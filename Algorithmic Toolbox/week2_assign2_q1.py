#python3

def fibo_calc(n):
    if (n==0):
        return 0

    if (n==1):
        return 1
    x=0
    y=1
    for i in range(1, n):
        i=x+y
        x=y
        y=i
    return i

n=int(input())
ans=fibo_calc(n)
print(ans)

