#python3

def fibo_calc(n):
    if (n==0):
        return 0

    if (n==1):
        return 1
    x=0
    y=1
    for i in range(1, n):
        x,y=y,(x+y)%10
    return y

n=int(input())
ans=fibo_calc(n)
print(ans%10)

