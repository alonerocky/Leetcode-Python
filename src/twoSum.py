def twoSum(num, target):
    result = ()
    if num == None or len(num) <2 :
        return result
    hashmap = {}
    for i in range(0,len(num)):
        one = num[i]
        theother = target - one
        if theother in hashmap:
            index = hashmap[theother]
            if index <= i:
                result = (index+1, i+1)
            else:
                result = (i+1, index+1)
        else:
            hashmap[one]=i
    print(result)
    return result


num = [2, 7, 11, 15]
twoSum(num,9)