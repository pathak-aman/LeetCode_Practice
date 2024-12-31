from math import inf

def min_in_rotated_array(arr):
    l, r = 0, len(arr) - 1
    min_num = inf
    while l <= r:
        mid = (l+r) // 2


        # Sorted section, directly store arr[l]
        if arr[l] <= arr[mid] <= arr[r]:
            min_num = min(min_num, arr[l])
            break

        # Identify the sorted half
        # Elimiate it but check the min before moving l, r pointers




        if arr[l] <= arr[mid]:
            min_num = min(min_num, arr[l])
            l = mid + 1
        elif arr[mid] <= arr[r]:
            min_num = min(min_num, arr[mid])
            r = mid - 1

    return min_num


if __name__ == "__main__":
    arrays = [
        [7,8,9,1,2,3,4,5,6],
        [4,5,1,2,3],
        [-100,6,10,78,100,-200],
        [36,100,2000,8999,-99999, -90, -9, 0]

    ]

    for array in arrays:
        print(array, min_in_rotated_array(array))

#        l,r          
# [7,8,9,1,2,3,4,5,6], 1

#   l    l   m    r     m               r
#  [36,100,2000,8999,-99999, -90, -9, 0], -99999