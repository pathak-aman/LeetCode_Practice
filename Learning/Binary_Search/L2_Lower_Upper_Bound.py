# Lower bound: smallest index "n" such that, arr[n] >= target

def lb(arr, target):
    l = 0
    r = len(arr) - 1
    ans = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            # l      t m           r
            # [1,3,4,5,6,17,28,89,110]
            #  l m   r
            #     l,m r
            ans = mid
            r = mid -1
        else:
            l = mid + 1
    return ans

# Upper Bound: smallest index "n" such that, arr[n] > target

def ub(arr, target):
    l = 0
    r = len(arr) - 1
    ans = len(arr) - 1
    # l      t m           r
    # [1,3,4,5,6,17,28,89,110]
    #  l m   r
    #     l,m r
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            # l      t m           r
            # [1,3,4,5,6,17,28,89,110]
            #  l m   r
            #     l,m r
            ans = mid
            r = mid -1
        else:
            l = mid + 1
    return ans


def search_insert(array, target):
    return lb(array, target)


def floor():
    return


if __name__ == "__main__":
    array = [5, 5,5,5, 7,7,7,7, 8, 8, 8,8,8,8,9,9,9,9,9,10,12,12,14,15,16,16,16,20]
    target = 6
    print(lb(array, target))
    print(ub(array, target))
    print(search_insert(array, target))