# Floor: Largest element less than or equal to target
def floor(array, target):
    l = 0
    r = len(array) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    if ans == -1:
        return -1
    return array[ans]


# Smallest element greater than or equal to target
def ceil(array, target):
    l = 0
    r = len(array) - 1
    ans = len(array)

    while l <= r:
        mid = (l + r) // 2
        if array[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    if ans == len(array):
        return ans
    return array[ans]

        # l      t m           r
        # [1,3,4,5,6,17,28,89,110]
        #  l m   r
        #     l,m r




if __name__ == "__main__":
    array = [3,4,4,7,8,10]
    target = 24
    print(floor(array, target))
    print(ceil(array, target))