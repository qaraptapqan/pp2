n = int(input("Enter limit: "))

nums = [True] * n
_ = 2
while _*_ < n:
    if nums[_]:
        for i in range(_+_, n, _):
            nums[i] = False
    _+=1
primes = [_ for _ in range(2,n) if nums[_]]\


l = list(map(int, input("Enter nums: ").split()))
r = list(filter(lambda x: x in primes, l))
print(r)
