
class Math:
    def add(self):
        n1=eval(input('enter number1'))
        n2=eval(input('enter number 2'))
        return n1+n2
    def sub(self):
        n1=eval(input('enter here'))
        n2=eval(input('enter here'))
        return n2-n1
obj=Math()
add=obj.add()
sub=obj.sub()
print(f'add:{add},sub:{sub}')