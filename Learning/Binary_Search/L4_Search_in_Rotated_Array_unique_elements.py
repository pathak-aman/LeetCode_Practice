def rotated_BS(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return mid
        # Identify the sorted half
        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                r = mid -1
            else:
                l = mid +1
        else:
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


if __name__ == "__main__":
    array = [7,8,9,1,2,3,4,5,6]
    targets = [1,3,5,8,2,0,6,3]

    for target in targets:
        print(target, rotated_BS(array, target))

