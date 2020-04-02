# functions
"""
def function_name(argument1, argument2):
    return argument1 + argument2

x = function_name(2, 8)
y = function_name(x, 21)
print(y)
print(type(function_name))
print(id(function_name))
"""

"""
def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result

def sum(a, b):
    return a + b

y = sum(14, 29)
z = list_sum([1, 2, 3])
print(y)
print(z)
"""

# stack in python
"""
def g():
    print("I am function g")
def f():
    print("I am function f")
    g()
    print("I am function f")

print("I am outside of any function")
f()
print("I am outside of any function")
"""

# task 1 - write program
# my code
"""
def closest_mod_5(x):
    x = int(x)
    while x % 5:
        x += 1
    return x
"""

# my optimized code
"""
def closest_mod_5(x):
    return (x + 4) // 5 * 5

y = int(input())
print(closest_mod_5(y))
"""

# fibonacci
"""
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

y = fib(5)
print(y)
"""

# task 2 - write program
"""
def C(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


n, k = map(int, input().split())
print(C(n, k))
"""