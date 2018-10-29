import operator

def is_operand(ch):
    return ch.isdigit()
def is_operator(ch):
    return ch in ['^', '*', '/', '+', '-']
def check_sign(s):
    "Handle --++1 case"
    result = []
    for i in range(len(s)):
        if (i==0 and (s[i]=='+' or s[i]=='-')) or (is_operator(s[i-1]) and (s[i]=='+' or s[i]=='-')) or (s[i-1]=='(' and (s[i]=='+' or s[i]=='-')):
            result.append('true')
        else:
            result.append('false')
    return result

def to_binary_op(s):
    s = s.replace(' ', '')
    result = check_sign(s)
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
def assign_class(item):
   switcher = {
           '+': add(),
           '-': sub(),
           '*': mul(),
           '/': div(),
           '^': pow(),
           '!': fac(),
           'sin': sin(),
           'cos': cos(),
           'tan': tan(),
           'cot': cot(),
           '(': leftParenthese(),
           ')': rightParenthese()
           }
   return switcher.get(item, Number(item))
def preprocess(s):
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
        elif string not in ['^', '*', '/', '+', '-', '!', 'sin', 'cos', 'tan', 'cot', '(', ')']:
            i = i + 1
        else:
            l.append(string)
            i = 0
            s = s.replace(string, '', 1)
            string = ''
    object_list = []
    for item in l:
        object_list.append(assign_class(item))
    return object_list

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
            if class_name == 'pow':
                stack.append(x.pow(y))
            elif class_name == 'mul':
                stack.append(x*y)
            elif class_name == 'div':
                stack.append(y/x)
            elif class_name == 'add':
                stack.append(x+y)
            else:
                stack.append(y-x)
        else:
            x = Number(float(stack.pop().val))
            if class_name == 'fac':
                stack.append(x.fac())
            elif class_name == 'cos':
                stack.append(x.cos())
            elif class_name == 'sin':
                stack.append(x.sin())
            elif class_name == 'tan':
                stack.append(x.tan())
            else:
                stack.append(x.cot())
    return stack.pop()
if __name__ == "__main__":
    s = '(5!)/(3!) - -2*cos(1*2/3) + sin(2!)*tan(1/3!)'
    new_s = to_binary_op(s)
    ob_list = preprocess(new_s)
    u = to_postfix(ob_list)
    v = calc(u)
    print(v.val)