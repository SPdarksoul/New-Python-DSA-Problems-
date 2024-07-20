def floorSqrt(n):
    if n == 0 or n == 1:
        return n
    s, e = 1, n
    ans = 1
    while s <= e:
        mid = s + (e - s) // 2
        if mid <= n / mid:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans

n = int(input("Enter a number: "))
print(floorSqrt(n))
