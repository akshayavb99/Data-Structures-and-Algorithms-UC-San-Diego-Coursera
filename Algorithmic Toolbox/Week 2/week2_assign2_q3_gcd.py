#python3

def gcd_calc(a,b):
    while (b>0):
        temp=b
        b=a%b
        a=temp
    return a

x,y=map(int, input().split())
ans=gcd_calc(x,y)
print(ans)