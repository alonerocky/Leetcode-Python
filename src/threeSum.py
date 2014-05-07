#from sets import Set
def threeSum(num):
    result = []
    if num == None or len(num) <= 2:
        return result
    num.sort()
    s = set()
    for i in range(0,len(num)):
        j = i+1
        k = len(num) -1
        while j < k:
            target = num[i] + num[j] + num[k]
            if target == 0:
                t = (num[i],num[j],num[k])
                if t not in s:
                    s.add(t)
                    result.append(list(t))
                j += 1
                k -= 1
            elif target < 0:
                j += 1
            else:
                k -= 1
    return result

num = [-1, 0, 1, 2, -1, -4]
print(threeSum(num))