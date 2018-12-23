#python3

n=int(input())
nums=[]
k=n
m=1
if n==1 or n==0:
    nums.append(n)
else:
    for i in range(1,k):
        if k<=2*m:
            nums.append(k)
            break
        else:
            nums.append(m)
            k=k-m
            m=m+1
print(m)
for i in range(m):
    print(nums[i], end=" ")