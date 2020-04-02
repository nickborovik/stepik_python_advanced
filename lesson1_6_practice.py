# task 1 - parent classes
# my code
"""
def function(x, y=[]):
    if y in dct:
        if x == y:
            return 'Yes'

        for j in dct[y]:
            if x == j or function(x, j) == 'Yes':
                return 'Yes'

    return 'No'


n = int(input())
classes, relation, answer, dct = [], [], [], {}

for _ in range(n):
    classes = input().split()
    if len(classes) == 1:
        dct[classes[0]] = []
    else:
        dct[classes[0]] = classes[2::]
        for k in dct[classes[0]]:
            if k not in dct:
                dct[k] = []

n = int(input())

for i in range(n):
    relation = input().split()
    if len(relation) > 1:
        answer.append(function(relation[0], relation[1]))
    else:
        answer.append('Yes')
print(*answer, sep='\n')
"""

# optimized code
"""
n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")
"""

# my optimized code
"""
def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

n = int(input())

parents = {}

for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2::]


q = int(input())
for _ in range(q):
    a, b = input().split()
    print('Yes' if is_parent(b, a) else 'No')
"""

# task 2 - Extended stack
"""
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())
"""

# task 3 - Logging
"""
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, line):
        list.append(self, line)
        self.log(line)
"""