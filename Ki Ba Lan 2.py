import math
binary_operators = ['^', '*', '/', '+', '-']
unary_operators = ['sin', 'cos', 'tan', 'cot']
parenthese = ['(', ')']
def is_operand(ch):
    return ch.isdigit()
def is_binary_operators(ch):
    return ch in binary_operators
def is_unary_operators(ch):
    return ch in unary_operators
def is_operator(ch):
    return ch in ['^', '*', '/', '+', '-']
def get_priority(item):
    if item in unary_operators:
        return 4
    elif item == '^':
        return 3
    elif item in ['*', '/']:
        return 2
    elif item in ['+', '-']:
        return 1
    else: 
        return 0
def check_incre_decre_op(s):
    result = []
    for i in range(len(s)):
        if (i==0 and (s[i]=='+' or s[i]=='-')) or (is_operator(s[i-1]) and (s[i]=='+' or s[i]=='-')) or (s[i-1]=='(' and (s[i]=='+' or s[i]=='-')):
            result.append('true')
        else:
            result.append('false')
    return result       

def convert_unary_to_binary_op(s):
    s = s.replace(' ', '')
    result = check_incre_decre_op(s)
    new_str = ''
    
    for i in range(len(s)):
        if result[i] == 'true':
            if s[i] == '-':
                new_str = new_str + '(0-1)*'
            else:    # s[i] == '-'
                pass
        else:
            new_str = new_str + s[i]
    return new_str
    
def preprocess(s):
    s = s.replace(' ', '')
    string = ''
    l = []
    i = 0
    while s != '':
        string = string + s[i]
#        print(string)
        if is_operand(string):
            l.append(string)
            i = 0
            s = s.replace(string, '', 1)
            string = ''
        elif string not in binary_operators + unary_operators + parenthese:
            i = i + 1
        else:
            l.append(string)
            i = 0
            s = s.replace(string, '', 1)
            string = ''
    return l

def to_postfix(l):
    P = []
    S = []
    for item in l:
        if is_operand(item):
            P.append(item)
        elif item == ')':
            op = S.pop()
            while op != '(' : #and len(S) > 0
                P.append(op)
                op = S.pop()
        else:
            if item == '(':
                S.append(item)
            else:
                while len(S) > 0 and get_priority(S[-1]) >= get_priority(item):
                    op = S.pop()
                    P.append(op)
                S.append(item)
            
    return P + list(reversed(S))

def calc(U):
    stack = []
    for item in U:
        if is_operand(item):
            stack.append(item)
        elif is_binary_operators(item):
            x = float(stack.pop())
            y = float(stack.pop())
            if item == '^':
                stack.append(math.pow(y, x))
            elif item == '*':
                stack.append(x*y)
            elif item == '/':
                stack.append(y/x)
            elif item == '+':
                stack.append(x+y)
            else:
                stack.append(y-x)
        else:
            x = float(stack.pop())
            if item == 'cos':
                stack.append(math.cos(x))
            elif item == 'sin':
                stack.append(math.sin(x))
            elif item == 'tan':
                stack.append(math.tan(x))
            else:
                stack.append(1/math.tan(x))
#    for item in stack:
#        print(item)
    return stack.pop()
#s = '2^(--3) - -10*cos(0*20/3) + tan(sin(0))'
s = '10+1-3'
s2 = convert_unary_to_binary_op(s)
l = preprocess(s2)
U = to_postfix(l)
v = calc(U)
print(v)