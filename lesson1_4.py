# task 1 - local variables
"""
t_c = 18
tmp = 'ok'

def fahrenheit(t_c):
    tmp = t_c * 9 / 5
    return tmp + 32

print(fahrenheit(t_c))
print(tmp)
"""

# task 2 - global variables
"""
ok_status = True
vowels = ['a', 'e', 'u', 'o', 'i']

def check(word):
    global ok_status
    for vowel in vowels:
        if vowel in word:
            return True
    ok_status = False
    return False

print(check('abacaba'))
print(ok_status)
print(check('www'))
print(ok_status)
"""


# task 3 - write program namespaces
# my code
"""
def create(namespace, parent):
    _namespaces[namespace] = parent
    _variables[namespace] = set()


def add(namespace, value):
        _variables[namespace].add(value)


def get(parent, value):
    if value in _variables[parent]:
        print(parent)
    elif parent == 'global' and value not in _variables[parent]:
        print(None)
    else:
        get(_namespaces[parent], value)


_namespaces, _variables = {'global': None}, {'global': set()}

for _ in range(int(input())):

    command, namespace, value = input().split()

    if command == 'create':
        create(namespace, value)

    elif command == 'add':
        add(namespace, value)

    elif command == 'get':
        get(namespace, value)
"""

# optimized code
"""
n = int(input())

parent = {"global": None}
vs = {"global": set()}

for _ in range(n):
    t, fst, snd = input().split()
    if t == "create":
        parent[fst] = snd
        vs[fst] = set()
    elif t == "add":
        vs[fst].add(snd)
    else:  # t == get
        while fst is not None:
            if snd in vs[fst]:
                break
            fst = parent[fst]
        print(fst)
"""

# my optimized code
"""
n = int(input())

parent = {'global': None}
vs = {'global': set()}

for _ in range(n):
    cmd, fst, snd = input().split()
    if cmd == 'create':
        parent[fst] = snd
        vs[fst] = set()
    elif cmd == 'add':
        vs[fst].add(snd)
    else:
        while fst is not None:
            if snd in vs[fst]:
                break
            fst = parent[fst]
        print(fst)
"""