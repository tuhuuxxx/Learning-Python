import math
class Number:
    def __init__(self, val=None):
        self.val = val
class Base:
    def __init__(self, prior, type_op):
        self.prior = prior
        self.type = type_op
    # def calc():
    #     raise NotImplementedError("")
class add(Base):
    def __init__(self):
        Base.__init__(self, 1, 'binary')
    def calc(self,a, b):
        c = Number()
        c.val = a.val + b.val
        return c
class sub(Base):
    def __init__(self):
        Base.__init__(self, 1, 'binary')
    def calc(self,a, b):
        c = Number()
        c.val = a.val - b.val
        return c
class mul(Base):
    def __init__(self):
        Base.__init__(self, 2, 'binary')
    def calc(self,a, b):
        c = Number()
        c.val = a.val*b.val
        return c
class div(Base):
    def __init__(self):
        Base.__init__(self, 2, 'binary')
    def calc(self,a, b):
        c = Number()
        c.val = a.val/b.val
        return c
class pow(Base):
    def __init__(self):
        Base.__init__(self, 3, 'binary')
    def calc(self,a, b):
        c = Number()
        c.val = a.val**b.val
        return c
class factorial(Base):
    def __init__(self):
        Base.__init__(self, 4, 'unary')   
    def calc(self,a):
        c = Number()
        c.val = math.factorial(a.val)
        return c
class tan(Base):
    def __init__(self):
        Base.__init__(self, 4, 'unary')   
    def calc(self,a):
        c = Number()
        c.val = math.tan(a.val)
        return c
class sin(Base):
    def __init__(self):
        Base.__init__(self, 4, 'unary')   
    def calc(self,a):
        c = Number()
        c.val = math.sin(a.val)
        return c
class cos(Base):
    def __init__(self):
        Base.__init__(self, 4, 'unary')   
    def calc(self,a):
        c = Number()
        c.val = math.cos(a.val)
        return c
class cot(Base):
    def __init__(self):
        Base.__init__(self, 4, 'unary')   
    def calc(self,a):
        c = Number()
        c.val = math.cos(a.val)/math.sin(a.val)
        return c
class leftParenthese(Base):
    def __init__(self):
        Base.__init__(self, 0, 'leftParenthese')
class rightParenthese(Base):
    def __init__(self):
        Base.__init__(self, 0, 'rightParenthese')