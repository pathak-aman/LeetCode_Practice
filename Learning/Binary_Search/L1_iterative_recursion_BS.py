def BS_iter(array, target):
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
                r = mid - 1
        else:
             l = mid + 1
    
    return -1


def BS_recu(array, l, r, target):
    if l > r:
         return -1
    mid = (l + r) // 2
    if array[mid] == target:
         return mid
    elif array[mid] > target:
        return BS_recu(array, l, mid - 1, target)
    return BS_recu(array, mid + 1, r, target)



if __name__ == "__main__":
    array = [2,4,6,7,12,17,24,28,58,79]
    # target = 67
    target = 24
    print(BS_iter(array, target))
    print(BS_recu(array, 0, len(array)-1, target))