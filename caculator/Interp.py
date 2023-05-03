import math


try:
    from nodes import *
except:
    from caculator.nodes import *
class tokenize:
    def __init__(self,input):
        self.input=iter(input)
        self.advance()
        self.isdigit='1234567890.'
        self.num=''
        self.new=[]
        self.op='+-*/^()'
        self.alpha='abcdefghijklmnopqrstuvwxyz'
        self.func=''
    def advance(self):
        try:
            self.current=next(self.input)
        except:
            self.current=None
    def generate(self):
        while self.current!=None:
            if self.current in self.isdigit:
                self.num+=self.current
            else:
                if self.current in self.op and self.num!='':
                    
                    self.new.append(float(self.num))
                    self.num=''
            if self.current in self.alpha:
                self.func+=self.current
            else:
                if self.current not in self.alpha and self.func!='':
                    print(self.func)
                        
                    self.new.append(self.get_func())
                    self.func=''  
            if self.current in self.op:
                self.new.append(self.current)
            
                
            self.advance()
        if self.num!='':
            self.new.append(float(self.num))
        if self.func!='':
            self.new.append(self.get_func())
        print(self.new)
        return self.new
    def get_func(self):
        if self.func=='pi':
            return math.pi
        elif self.func=='tan':
            return 'tan'
        elif self.func=='sin':
            return 'tan'
        elif self.func=='cos':
            return 'cos'
        else:
            return None
        

class Parse:
    def __init__(self,tokenized):
        self.tokenized=iter(tokenized)
        self.op='+-*/^()'
        self.advance()
        self.tree=[]
    def advance(self):
        try:
            self.current=next(self.tokenized)
        except:
            self.current=None
    def parse(self):
        if self.current==None:
            return None
        result=self.expr()
        if self.current!=None:
            print('error')

        return result
    def expr(self):
        result=self.term()
        while self.current!=None and self.current in ("+",'-'):
            if self.current =='+':
                self.advance()
                result=addnode(result,self.term())
            elif self.current=='-':
                self.advance()
                result=subnode(result,self.term())
                
        self.tree.append(result)
        return result
    def term(self):
        result=self.exo()
        while self.current!=None and self.current in ("*",'/'):
            if self.current =='*':
                self.advance()
                result=timesnode(result,self.exo())
            elif self.current=='/':
                self.advance()
                result=dividenode(result,self.exo())

        self.tree.append(result)

        return result
    def exo(self):
        result=self.factor()
        while self.current!=None and self.current in ('^'):
            if self.current=='^':
                self.advance()
                result=powernode(result,self.factor())
        self.tree.append(result)

        return result
    def factor(self):
        tok=self.current
        #print(tok)
        if type(tok)==float:
                self.advance()
                self.tree.append(num(tok))
                return num(tok)
        elif tok=='(':
            self.advance()
            result=self.expr()
            if self.current!=')':
                print('error')
            self.advance()
            self.tree.append(result)
            return result
        elif tok=='-':
            self.advance()
            #self.tree.append(minusnode(self.factor()))
            return minusnode(self.factor())
        elif tok=='+':
            self.advance()
            #self.tree.append(plusnode(self.factor()))
            return plusnode(self.factor())
        print(self.current)
        print('erro')
class interp:
    def __init__(self,tree):
        self.tree=tree
        self.current=None
        self.visited=[]
    def traverse(self,root):
        try:
            if root.id=='num':
                return float(root.x)
            elif root.id=='neg':
                #rint(-float(root.x.x))
                return -self.traverse(root.x)
            elif root.id=='pos':
                #rint(-float(root.x.x))
                return abs(float(root.x.x))
            if root.id=='add':
                an=self.traverse(root.left)+self.traverse(root.right)

                return an
            elif root.id=='sub':
                an=self.traverse(root.left)-self.traverse(root.right)

                return an
            if root.id=='power':
                an=self.traverse(root.left)**self.traverse(root.right)
                return an
            if root.id=='times':
                an=self.traverse(root.left)*self.traverse(root.right)

                return an
            elif root.id=='divide':
                an=self.traverse(root.left)/self.traverse(root.right)

                return an


        except Exception as e:
            print(e)


if __name__=='__main__':
    while True:
        calc=input("> ")
        t=tokenize(calc).generate()
        p=Parse(t).parse()
        i=interp(p)
        print(i.traverse(p))
    
