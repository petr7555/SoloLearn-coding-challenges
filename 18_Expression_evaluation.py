import operator

def evaluate(string):
    operators = ["+", "-", "*", "/"]
    operand_stack = []
    operator_stack = []
    precedence = {"+": 0,"-": 0,"*": 1,"/": 1, "(": -1, ")": 2}
    ops = {"+": operator.add, "-": operator.sub,'*' : operator.mul, '/' : operator.truediv}
    exp = "".join(string.split())
    for c in exp:
        if c == "(":
            operator_stack.append(c)
        elif c == ")":
            while operator_stack[-1] != "(":
                value1 = float(operand_stack.pop())
                op = operator_stack.pop()
                value2 = float(operand_stack.pop())
                operand_stack.append(ops[op](value2,value1))
            operator_stack.pop()
        elif c in operators:
            while operator_stack != [] and precedence[operator_stack[-1]] >=  precedence[c]:
                value1 = float(operand_stack.pop())
                op = operator_stack.pop()
                value2 = float(operand_stack.pop())
                operand_stack.append(ops[op](value2,value1))
            operator_stack.append(c)
        else:
            operand_stack.append(c)
    while operator_stack != []:
        value1 = float(operand_stack.pop())
        op = operator_stack.pop()
        value2 = float(operand_stack.pop())
        operand_stack.append(ops[op](value2,value1))
    
    return operand_stack[0]
    
print(evaluate("6/(4 + 1)"))
