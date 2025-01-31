res = []

def is_prime(num: int) -> bool:
    global res
    if num in res: return False
    if num <= 1:
        return False
    elif num <= 3:
        res.append(num)
        return True
    elif num%2 == 0:
        return False


    i = 3
    while i*i <= num:
        if num%i == 0:
            return False
        i+=2
    res.append(num)
    return True

def filter_prime(nums: list[int]) -> list[int]:
    return [_ for _ in nums if is_prime(_)]

if __name__ == '__main__':
    while 1:
        try:
            l = list(map(int, input("Enter nums: ").split()))
            t = filter_prime(l)
            print(t)
            res.clear()
        except Exception as ex:
            break
