def rotated_BS_with_dups(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return True
        
        # Check edge cases, shrink the search space
        if arr[l] == arr[mid] == arr[r]:
            l += 1
            r -= 1
            continue

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
    return False


if __name__ == "__main__":
    # array = [7,7,7,7,7,7,7,7,7,7,7,8,8,8,9,1,2,3,4,5,6,7,7,7,7,7]
    # targets = [7, 1,3,5,8,2,0,6,3]

    array = [4,5,1,2,3]
    targets = [1,2,3,4,5,6,7,8,9]
    for target in targets:
        print(target, rotated_BS_with_dups(array, target))

