# Classes
"""
class MyClass:
    a = 10

    def func(self):
        print('Hello')

x = MyClass()
print(type(x))
print(type(MyClass))
print(MyClass.a)
"""

# Classes 2
"""
class Counter:
    pass

Counter
x = Counter()
x.count = 0
x.count += 1
"""

# Classes 3
"""
class Counter:
    def __init__(self):
        self.count = 0

Counter
x = Counter()
print(x.count)
x.count += 1
print(x.count)
"""

# Classes 4
"""
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0

Counter # Class object
x = Counter()
x.inc()
print(x.count)
Counter.inc(x)
print(x.count)
x.reset()
print(x.count)
"""

# Task 1 - write program Kopilka (MoneyBox)
"""
class MoneyBox:
    def __init__(self, capacity):  # конструктор с аргументом – вместимость копилки
        self.storage = 0
        self.capacity = capacity

    def can_add(self, v):  # True, если можно добавить v монет, False иначе
        if self.storage + v <= self.capacity:
            return True
        return False

    def add(self, v):  # положить v монет в копилку
        if self.can_add(v):
            self.storage += v
        else:
            print('Storage is full')
"""

# Task 2 - write program Buffer
"""
class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        for i in a:
            self.buffer.append(i)
            if len(self.buffer) == 5:
                print(sum(self.buffer))
                self.buffer.clear()

    def get_current_part(self):
        return self.buffer

# test
x = Buffer()
x.add(1, 2, 3, 4, 5)
x.get_current_part()
"""

# Classes 5
"""
class Song:

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = []

    def add_tags(self, *args):
        self.tags.extend(args)

song1 = Song("Shakey Graves", "Roll the Bones")
song1.add_tags("Americana", "Country")

song2 = Song("Neuromonah Feofan", "Holodno v lesu")
song2.add_tags("Russian", "Drum'n'base")

print(song2.tags)
"""

# Classes 6
"""
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)
"""