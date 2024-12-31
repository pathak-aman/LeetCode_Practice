# Nth Root of a Number using Binary Search
# Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

def nth_root(n, num):
    l = 1
    r = num

    while l <= r:
        mid = (l + r) // 2
        if mid ** n == num:
            return mid
        elif mid ** n < num:
            l = mid + 1
        else:
            r = mid - 1
    return -1


nums = [100,64,27,8,16,243,10000,256,729, 625, 4096]
nth = [10,3,3,3,4,5,2,4,9,5,16]
for n, num in zip(nth, nums):
    print(nth_root(n, num))




