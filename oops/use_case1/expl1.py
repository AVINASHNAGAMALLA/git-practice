
class math_func:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return (self.a+self.b)
    def sub(self):
        return (self.a-self.b)
obj=math_func(200,100)

if __name__=='__main__':
    add=math_func(20,10).add()
    sub=math_func(20,10).sub()
    print(add,sub)