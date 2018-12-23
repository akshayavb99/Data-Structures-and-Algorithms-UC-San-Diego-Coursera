#python3

n=int(input())
num=list(map(int, input().split()))

def sorting_algo(i):
    div=9
    while div<i:
        div=div*10+9

    return i/div

final=sorted(num,key=sorting_algo,reverse=True)
for i in range(n):
    print(final[i],end="")