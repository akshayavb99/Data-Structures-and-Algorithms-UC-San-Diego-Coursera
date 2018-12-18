#python3

def min_coins(n):
    sum=0
    rem_ten=n%10
    sum+=(n-rem_ten)/10
    rem_five=rem_ten%5
    sum+=(rem_ten-rem_five)/5
    sum+=rem_five
    return sum

m=int(input())
ans=min_coins(m)
print(int(ans))
