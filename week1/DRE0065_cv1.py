def precedence(op):
    if op in "+-": return 1
    elif op in "*/": return 2
    return 0

def apply_op(x, y, op):
    if op == '+': return x+y
    elif op == '-': return x-y
    elif op == '*': return x*y
    elif op == '/':
        if y == 0: return "ERROR"
        return x//y
    return None

def compute_top(nums, opes):
    if len(nums) < 2: return "ERROR"
    y, x, op = nums.pop(), nums.pop(), opes.pop()
    
    rst = apply_op(x, y, op)
    if rst == "ERROR": return "ERROR"
    
    nums.append(rst)
    return None

def is_invalid(expr):
    for i in range(len(expr) - 1):
        if expr[i] in "+-*/" and expr[i+1] in "+*/": return True
        if expr[i] == '(' and expr[i+1] in "+*/": return True
        if expr[i] in "+*/" and expr[i+1] == ')': return True
        if expr[i] == '(' and expr[i+1] == '-': return True
    return False

def evaluate_rst(expr):
    expr = expr.replace(" ","")
    
    if any(z not in "0123456789+-*/()" for z in expr): return "ERROR"
    if expr.count('(') != expr.count(')'): return "ERROR"
    if is_invalid(expr): return "ERROR"
    
    nums, opes, i = [], [], 0
    while i < len(expr):
        c = expr[i]
        
        if c.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            nums.append(num)
            i -= 1 
        elif c in "+-*/":
            if i == 0 or i == len(expr) - 1 or expr[i-1] in "+-*/(": return "ERROR"
            while opes and precedence(opes[-1]) >= precedence(c):
                if compute_top(nums, opes) == "ERROR": return "ERROR"
            opes.append(c) 
        elif c == '(':
            if i < len(expr) - 1 and expr[i+1] in "*/)": return "ERROR"
            opes.append(c)
        elif c == ')':
            if i > 0 and expr[i-1] in "+-*/(": return "ERROR"
            while opes and opes[-1] != '(':
                if compute_top(nums, opes) == "ERROR": return "ERROR"
            if not opes or opes.pop() != '(': return "ERROR"  
        else: return "ERROR"
        i += 1
    
    while opes:
        if len(nums) < 2 or opes[-1] in "()": return "ERROR"
        if compute_top(nums, opes) == "ERROR": return "ERROR"
    
    if len(nums) == 1: return nums[0]
    else: return "ERROR"

n = int(input().strip())
for _ in range(n):
    expr = input().strip()
    print(evaluate_rst(expr))