'''class MyClass:
    A sample example class
    i= 123456
    def f(self):
        return  'hello world'
x=MyClass()
print(x.i,x.f())
class Complex:
    def __init__(self,realpart,imapart):
        self.r=realpart
        self.i=imapart
x=Complex(3.0,-4.5)
print(x.r,x.i)
print(issubclass(bool,int))'''
class Reverse:
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]
rec=Reverse('abcdef')
for char in  rec:
    print(char)
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
for char in reverse('golf'):
    print(char)