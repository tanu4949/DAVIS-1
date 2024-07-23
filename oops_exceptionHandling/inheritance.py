#python program for hybrid inheritence
class A:
    def show(self):
        print("this is show method")
class B(A):
    def demo(self):
        print("demo method")
class C(A):
    pass
class D(B,C):
    pass

obj=C()
obj.show()
