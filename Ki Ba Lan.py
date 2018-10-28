# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 20:46:47 2018

@author: dang tu
"""
operators = ['*', '/', '+', '-', ')', '(']
priorities = [2, 2, 1, 1, 0, 0]
def is_Operator(ch):
    return ch in ['*', '/', '+', '-']
def check_unary_operator(s):
    result = []
    for i in range(len(s)):
        if (i==0 and (s[i]=='+' or s[i]=='-')) or (is_Operator(s[i-1]) and (s[i]=='+' or s[i]=='-')) or (s[i-1]=='(' and (s[i]=='+' or s[i]=='-')):
            result.append('true')
        else:
            result.append('false')
    return result       
def convert_unary_to_binary_op(s):
    result = check_unary_operator(s)
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

def isOperand(ch):
    return ch not in ['*', '/', '+', '-', '(', ')']
def get_priority(ch): 
    return priorities[operators.index(ch)]
def to_postfix(s):
    P = []
    S = []
    for ch in s:
        if isOperand(ch):
            P.append(ch)
        elif ch == ')':
            op = S.pop()
            while op != '(' : #and len(S) > 0
                P.append(op)
                op = S.pop()
        else:
            if ch == '(':
                S.append(ch)
            else:
                while len(S) > 0 and get_priority(S[-1]) >= get_priority(ch):
                    op = S.pop()
                    P.append(op)
                S.append(ch)
            
    return P + list(reversed(S))
def calc(s):
    U = to_postfix(s)
    stack = []
    for item in U:
        if isOperand(item):
            stack.append(item)
        else:
            x = float(stack.pop())
            y = float(stack.pop())
            if item == '*':
                stack.append(x*y)
            elif item == '/':
                stack.append(y/x)
            elif item == '+':
                stack.append(x+y)
            else:
                stack.append(y-x)
    return stack.pop()
if __name__ == "__main__":
    s = '(+2-3*4/5)+(-3)*5--2'
    new_s = convert_unary_to_binary_op(s)     
    value = calc(new_s)
    print(value)
