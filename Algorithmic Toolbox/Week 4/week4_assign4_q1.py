def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
            break
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return mid
    else: return -1


a_in=list(map(int,input().split()))
n=a_in[0]
a=a_in[1:]
b_in=list(map(int,input().split()))
k=b_in[0]
b=b_in[1:]
for i in range(k):
    print(binary_search(a, b[i]), end=" ")
