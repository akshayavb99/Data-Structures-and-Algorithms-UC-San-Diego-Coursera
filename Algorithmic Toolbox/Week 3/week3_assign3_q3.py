#python3

def revenue_gen():
    c=sorted(b)
    d=sorted(a)
    finalVal=0
    for i in range(n):
        finalVal=finalVal+(d[i]*c[i])

    print(finalVal)

n=int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
revenue_gen()