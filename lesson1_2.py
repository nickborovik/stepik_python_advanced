# task 1 - id
"""
x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))
"""

"""
x = [1, 2, 3]
y = x
print(y is x)
print(y is [1, 2, 3]) 
"""

"""
x = [1, 2, 3]
y = x
print(y is x)
x.append(4)
print(x)
print(y)
"""

# task 2 - question, append
"""
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"
print(str(x) + " " + s)
"""

# task 3 - type
"""
x = [1, 2, 3]
print(type(x))
print(type(4))
print(type(type(x)))
"""

# task 4 - write program
# my code
"""
_id = set()
for obj in objects:
    _id |= {id(obj)}
print(len(_id))
"""

# optimized code
"""
print(len(set(map(id, objects))))
"""

# my optimized code
"""
print(len(set(map(id, objects))))
"""