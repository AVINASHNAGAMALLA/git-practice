
#using innit constructor,so we can use for multiple
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return(self.a+self.b)
    def sub(self):
        return(self.a-self.b)
ob=calc(20,10)
add=ob.add()
sub=ob.sub()
print(add,sub)  