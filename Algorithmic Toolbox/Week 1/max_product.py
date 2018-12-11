#python3
def max_pair_prod():
    n = int(input())
    arr = [int(i) for i in input().split(' ')]

    max_index = -1
    for i in range(0, len(arr)):
        if max_index == -1 or arr[max_index] < arr[i]:
            max_index = i
    sec_max_index = -1
    for i in range(0, len(arr)):
        if (sec_max_index == -1 or arr[sec_max_index] < arr[i]) and i != max_index:
            sec_max_index = i

    print(arr[max_index] * arr[sec_max_index])


max_pair_prod()