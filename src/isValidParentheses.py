'''
Created on Jun 14, 2014

@author: shoulongli
'''

def isValid(s):
    if s == None or len(s) == 0:
        return False
    parentheses_left = ['(','[','{']
    parentheses_right = [')',']','}']
    stack = []
    for c in s:
        #print(c)
        print(stack)
        print(c)
        if c in parentheses_left or c in parentheses_right:
            if c in parentheses_left:
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack[len(stack) -1] != '(':
                    return False
                else:
                    stack.pop()
            elif c == ']':
                if len(stack) == 0 or stack[len(stack) -1] != '[':
                    return False
                else:
                    stack.pop()
            elif c == '}':
                if len(stack) == 0 or stack[len(stack) - 1] != '{':
                    return False
                else:
                    stack.pop()
        else:
            return False
    return len(stack) == 0


def isValidII( s):
        if s == None or len(s) == 0:
            return False
        parentheses_left = ['(','[','{']
        parentheses_right = [')',']','}']
        stack = []
        for c in s:
            if c in parentheses_left or c in parentheses_right:
                if c in parentheses_left:
                    stack.append(c)
                elif c == ')':
                    if len(stack) == 0 or stack[len(stack) -1] != '(':
                        return False
                    else:
                        stack.pop()
                elif c == ']':
                    if len(stack) == 0 or stack[len(stack) - 1] != '[':
                        return False
                    else:
                        stack.pop()
                elif c == '}':
                    if len(stack) == 0 or stack[len(stack) -1 ] != '{':
                        return False
                    else:
                        stack.pop()
            else:
                return False
        return len(stack) == 0
p = "()"
print(isValidII(p))

