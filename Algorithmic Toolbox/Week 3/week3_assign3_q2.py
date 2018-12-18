#python3

def val_decide():
    countW=W
    countVal=0.0

    vw=[v[i]/w[i] for i in range(0,n)]
    for i in range(n):
        for j in range(0, n - i - 1):
            if vw[j] < vw[j + 1]:
                vw[j], vw[j + 1] = vw[j + 1], vw[j]
                w[j],w[j+1]=w[j+1],w[j]
                v[j], v[j + 1] = v[j + 1], v[j]

    for i in range(n):
        if countW==0:
            return countVal

        if countW>=w[i]:
            countVal=countVal+vw[i]*w[i]
            countW=countW-w[i]
        else:
            countVal=countVal+vw[i]*countW
            countW=0

    return countVal


n,W=map(int,input().split(' '))
v=[0.0 for i in range(0,n)]
w=[0.0 for i in range(0,n)]
for i in range(0,n):
    v[i],w[i]=map(float,input().split(' '))
ans=val_decide()
print(ans)