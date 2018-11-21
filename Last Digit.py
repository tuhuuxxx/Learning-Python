import math
import time

def Mod(a, b) : 
    # type b: str
    mod = 0
    for i in range(len(b)) : 
        mod = (mod * 10 + (int)(b[i])) % a 
    return mod

def find_last_digit(a, b):
    a = str(a)
    b = str(b)
    len_a  = len(a)
    len_b = len(b)
    
    if len_a==1 and len_b==1 and a[0]=='0' and b[0]=='0': # 0^0
        return 1
    if len_b==1 and b[0]=='0': # a^0
        return 1
    if len_a==1 and a[0]=='0': # 0^b
        return 0
    
    if Mod(4, b) == 0:
        exp = 4
    else:
        exp = Mod(4, b)
        
    result = math.pow(int(a[len_a-1]), exp)
    return result%10

gt = 0
start = time.time()
for n in range(10**7):
    gt += find_last_digit(n, n)
end = time.time()
print(gt)
print(end-start)