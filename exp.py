class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v, Expr)
assert isinstance(v, Val)
assert not isinstance(v, int)

class Add(Expr):
    __slots__=['left','right']
    def __init__(self, a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()

e = Add(Val(1),Val(2))
assert e.eval() == 3

e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6



class Mul(Expr):
    __slots__=['left','right']
    def __init__(self, a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() * self.right.eval()

e = Mul(Val(1),Val(2))
assert e.eval() == 2

e = Mul(Val(1),Mul(Val(2),Val(3)))
assert e.eval() == 6


class Sub(Expr):
    __slots__=['left','right']
    def __init__(self, a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() - self.right.eval()

e = Sub(Val(1),Val(2))
assert e.eval() == -1

e = Sub(Val(1),Sub(Val(2),Val(3)))
assert e.eval() == 2


class Div(Expr):
    __slots__=['left','right']
    def __init__(self, a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() // self.right.eval()

e = Div(Val(7),Val(2))
assert e.eval() == 3

e = Div(Val(7),Div(Val(6),Val(3)))
assert e.eval() == 3


