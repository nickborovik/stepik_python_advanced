# Class parent 1
"""
class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0

x = MyList()
print(x)
x.extend([1, 2, 3, 4, 5])
print(x)
print(x.even_length())
x.append(6)
print(x.even_length())
"""

# Class parent 2
"""
class E: pass
class D: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

print(issubclass(A, A))
print(issubclass(C, D))
print(issubclass(A, D))
print(issubclass(C, object))
print(issubclass(object, C))
print()

x = A()
print(isinstance(x, A))
print(isinstance(x, B))
print(isinstance(x, object))
print(isinstance(x, str))
"""

# Class parent 3
"""
class E: pass
class D: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

print(A.mro())
"""

# Class parent 4
"""
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


print(MyList.mro())
x = MyList([1, 2, 3])
print(x.even_length())
x.append(4)
print(x.even_length())
"""

# Class parent 5
"""
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


class MyDict(dict, EvenLengthMixin):
    pass

x = MyDict()
x['key'] = 'value'
x['another key'] = 'another value'
print(x.even_length())
"""

# Class parent 6
"""
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()
        print('Last value is', x)
        return x


ml = MyList([1, 2, 4, 17])
z = ml.pop()
print(z)
print(ml)
"""

# Class parent 7
"""
class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)
"""

# Class parent 8
"""
class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()
"""
