class num:
    def __init__(self,x):
        self.x=str(x)
        self.id='num'
    def __repr__(self):
        return float(self.x)

class subnode:
    def __init__(self,x,y):
        self.left=x
        self.right=y
        self.id='sub'
    def __repr__(self):
        return f"({self.left} - {self.right})"
    def eval(self):
        return float(self.left.x)-float(self.right.x)
class tannode:
    def __init__(self,exp):
        self.exp=exp
        id='tan'
    def __repr__(self):
        return f'(tan({self.exp}))'
class powernode:
    def __init__(self,x,y):
        self.left=x
        self.right=y
        self.id='power'
    def __repr__(self):
        return f'({self.left}^{self.right})'
class addnode:
    def __init__(self,x,y):
        self.left=x
        self.right=y
        self.id='add'
    def __repr__(self):
        return f"({self.left} + {self.right})"
    def eval(self):
        return float(self.left.x)+float(self.right.x)
class timesnode:
    def __init__(self,x,y):
        self.left=x
        self.right=y
        self.id='times'
    def __repr__(self):
        return f"({self.left} * {self.right})"
    def eval(self):
        return float(self.left.x)*float(self.right.x)
class dividenode:
    def __init__(self,x,y):
        self.left=x
        self.right=y
        self.id='divide'
    def __repr__(self):
        return f"({self.left} / {self.right})"
    def eval(self):
        return float(self.left.x)/float(self.right.x)
    
class plusnode:
    def __init__(self,x):
        self.x=x
        self.id='pos'
    def __repr__(self):
        return f"+{self.x}"
    def eval(self):
        return abs(float(self.x))
class minusnode:
    def __init__(self,x):
        self.x=x
        self.id='neg'
    def __repr__(self):
        return f"(-{self.x})"
    def eval(self):
        return 0-float(self.x)
