# mistakes grammar
"""
print('This line executed')

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 'abc', 4, 17, 3])
ml.sort()
print(ml)
"""

# mistakes IndexError
"""
def f():
    x = [1, 2, 3]
    print(x[4])

f()
"""

# mistake with try / except
"""
try:
    x = [1, 2, 'hello', 7]
    x.sort()
    print(x)
except TypeError:
    print('Type error :( ')

print('I can catch')
"""


# mistake function with try / except
"""
def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type error')
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


print(f(5, 0))
print(f(5, []))
"""
"""
def f(x, y):
    try:
        return x / y
    except:
        print('Error :(')


print(f(5, 0))
print(f(5, []))
"""
"""
try:
    15 / 0
except ArithmeticError:
    print('ArithmeticError :(')

print(ZeroDivisionError.mro())
"""

# mistake finally
"""
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is', result)
    finally:
        print('finally')


divide(2, 1)
divide(2, 0)
divide(2, [])
"""

# task 1 - write program exeption

try:
    foo()
except ZeroDivisionError:
    print('ZeroDivisionError')
except AssertionError:
    print('AssertionError')
except ArithmeticError:
    print('ArithmeticError')
