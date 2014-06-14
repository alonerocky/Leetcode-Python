'''
Created on Jun 14, 2014

@author: shoulongli
'''
#["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
def evalRPN(tokens):
    if tokens == None or len(tokens) == 0:
        return 0
    operators = ["+","-","*","/"]
    stack = [] # use stack
    for token in tokens:
        if len(token) == 1 and token in operators: #operator
            op2 = stack.pop()
            op1 = stack.pop()
            result = 0.0
            if token == "+":
                result = int(float(op1) + float(op2))
            elif token == "-":
                result = int(float(op1) - float(op2))
            elif token == "*":
                result = int(float(op1) * float(op2))
            elif token == "/":
                result = int(float(op1) / float(op2))
            stack.append(str(result))
        else:
            stack.append(token)
        print(stack)
    return stack.pop()

tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["4", "13", "5", "/", "+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

#print(evalRPN(tokens1))
#print(evalRPN(tokens2))
print(evalRPN(tokens3))
print(6//-132)