def lower_bound(array, target):
    l,r = 0, len(array) -1
    ans = -1

    while l <= r:
        mid = (l+r) // 2
        if array[mid] >= target:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans

def upper_bound(array, target):
    l,r = 0, len(array) - 1
    ans = len(array)

    while l <= r:
        mid = (l+r) // 2
        if array[mid] > target:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans

def occurence(array, target):
    lb = lower_bound(array, target)
    if lb == len(array) or array[lb] != target:
        return 0
    ub = upper_bound(array, target)
    # print(ub,lb)
    return ub - lb

if __name__ == "__main__":
    array = [-33,-7,-7, -5 ,0,0,0,1, 4,4, 4, 8, 19, 19,19,25,25,25,25,25,90]
    print(len(array))
    targets = [-5, 2,8,14,18,25,99,-100, -33, 4, 0, 90]
    for target in targets:
        print(target, occurence(array, target))