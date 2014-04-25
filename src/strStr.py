# KMP
def strStr(string, pattern):
    if pattern == None or len(pattern) == 0:
        return string
    result = failure(pattern)
    i = 0;
    j = 0;
    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return string[i-j:]
        elif j > 0:
            j = result[j]
        else:
            i += 1
            j = 0
    return ''

def strStrII(string, pattern):
    if pattern == None or len(pattern) == 0:
        return string

    i = 0;
    j = 0
    while i + len(pattern) <= len(string):
        if string[i+j] == pattern[j]:
            j += 1
            if j == len(pattern):
                return string[i:]
        else:
            i += 1
            j = 0

    return ''


def failure(pattern):
    if pattern == None:
        return None

    result = [0] * len(pattern)
    result[0] = -1
    #result[0] = -1
    #result[i-1] = j
    i = 1
    j = -1
    while i < len(pattern):
        if j == -1 or pattern[i-1] == pattern[j]:
            result[i] = j+1
            i += 1
            j += 1
        elif j > 0:
            j = result[j]
        else:
            result[i] = 0
            i += 1
            j = 0

    return result

print(failure("abc"))
print(strStr("abababcdd","abc"))
print(strStrII("abababcdd","abc"))
