# Integer sqrt

def sqrt(n):
    l = 1
    r = n
    sqrt = 1

    while l <= r:
        mid = (l+r) // 2
        if mid * mid <= n:
            sqrt = max(sqrt, mid)
            l = mid + 1
        else:
            r = mid - 1
    return sqrt

if __name__ == "__main__":
    nums = [100,45,65,38,22,1,234,665,777,254,265,25,24,26]
    for num in nums:
        print(num, sqrt(num))