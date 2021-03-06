from op_class import *
import re

def is_operand(ch):
    return ch.isdigit()
def is_operator(ch):
    return ch in ['^', '*', '/', '+', '-']
def assign_class(item):
   switcher = {
           '+': add(),
           '-': sub(),
           '*': mul(),
           '/': div(),
           '^': pow(),
           '!': factorial(),
           'sin': sin(),
           'cos': cos(),
           'tan': tan(),
           'cot': cot(),
           '(': leftParenthese(),
           ')': rightParenthese()
           }
   return switcher.get(item, Number(item))
def preprocess(s):
    s = s.replace(' ', '')
    
    flag = []
    for i in range(len(s)):
        if (i==0 and (s[i]=='+' or s[i]=='-')) or (is_operator(s[i-1]) and (s[i]=='+' or s[i]=='-')) or (s[i-1]=='(' and (s[i]=='+' or s[i]=='-')):
            flag.append('true')
        else:
            flag.append('false')
    new_str = ''
    for i in range(len(s)):
        if flag[i] == 'true':
            if s[i] == '-':
                new_str = new_str + '(0-1)*'
            else:    # s[i] == '-'
                pass
        else:
            new_str = new_str + s[i]
    new_str = new_str + ')'*(s.count('(') - s.count(')'))
    l = re.findall(r'[0-9]+\.[0-9]+|[0-9]+|[\+\-*/^!()/]|sin|cos|tan|cot', new_str)
    object_list = []
    for item in l:
        object_list.append(assign_class(item))
    
    u = [object_list[0]]
    for i in range(1, len(object_list)):
        if type(object_list[i]).__name__ == 'leftParenthese' and type(object_list[i-1]).__name__ in ['rightParenthese', 'Number', 'factorial']:
            u.append(mul())
            u.append(object_list[i])
        elif type(object_list[i]).__name__ in ['sin', 'cos', 'tan', 'cot'] and type(object_list[i-1]).__name__ in ['Number', 'factorial']:
            u.append(mul())
            u.append(object_list[i])
        else: 
            u.append(object_list[i])
    
    return u

def to_postfix(object_list):
    P = []
    S = []
    for item in object_list:
        class_name = type(item).__name__
        if class_name == 'Number':
            P.append(item)
        elif class_name == 'rightParenthese':
            op = S.pop()
            while type(op).__name__ != 'leftParenthese' : #and len(S) > 0
                P.append(op)
                op = S.pop()
        else:
            if class_name == 'leftParenthese':
                S.append(item)
            else:
                while len(S) > 0 and S[-1].prior >= item.prior:
                    op = S.pop()
                    P.append(op)
                S.append(item)
    
    return P + list(reversed(S))

def calc(U):
    stack = []
    for item in U:
        class_name = type(item).__name__
        if class_name == 'Number':
            stack.append(item)
        elif item.type == 'binary':
            x = Number(float(stack.pop().val))
            y = Number(float(stack.pop().val))
            stack.append(item.calc(y,x))
            # if class_name == 'pow':
            #     stack.append(pow.calc(y, x))
            # elif class_name == 'mul':
            #     stack.append(mul.calc(y, x))
            # elif class_name == 'div':
            #     stack.append(div.calc(y, x))
            # elif class_name == 'add':
            #     stack.append(add.calc(y, x))
            # else:
            #     stack.append(sub.calc(y, x))
        else:
            x = Number(float(stack.pop().val))
            stack.append(item.calc(x))
            # if class_name == 'factorial':
            #     y = factorial.calc(x)
            #     stack.append(y)
            # if class_name == 'cos':
            #     stack.append(cos.calc(x))
            # elif class_name == 'sin':
            #     stack.append(sin.calc(x))
            # elif class_name == 'tan':
            #     stack.append(tan.calc(x))
            # elif class_name == 'cot':
            #     stack.append(cot.calc(x))
#        for item in stack:
#            print(item)  
        
    return stack.pop()
def standardize(s='1+(3(('):
    s = s.replace(' ', '')
    count1 = s.count('(')
    count2 = s.count(')')
    new_str = ''
    for i in range(len(s)):
        if s[i] == '(' and s[i-1] and (s[i-1].isdigit() or s[i-1] == '!'):
            new_str = new_str + '*'  + s[i]
        else:
            new_str = new_str + s[i]
    s = new_str   
    s = s + ')'*(count1 - count2)
    print(s)
    ob_list = preprocess(s)
    u = to_postfix(ob_list)
    v = calc(u)
    print(v.val)
if __name__ == "__main__":
#    s = '+2^(--3!) - -+2.25*cos(0*20/3) + tan(sin(0.0))'
    s = '(2 + 3)(4 - 6.015)(cos(3!sin(20 -- 2/(3'
    ob_list = preprocess(s)
    u = to_postfix(ob_list)
    v = calc(u)
    print(v.val)