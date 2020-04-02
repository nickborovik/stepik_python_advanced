# task 1 - interpretator
"""
x = 15
y = 'hello'
print(x)
print(y)
print(x + y)
"""

# task 2 - write program
# my code
"""
a = 0
for _ in range(int(input())):
    a += int(input())
print(a)
"""

# optimized code
"""
print(sum(int(input()) for _ in range(int(input()))))
"""

# my optimized code
"""
print(sum((int(input()) for _ in range(int(input())))))
"""