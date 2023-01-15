# -*- coding: utf-8 -*-
# ex18.py

# this one is like your scripts with argv
def print_two(*args):  # 不太理解之类*的含义--> 将所有的参数收集到list args中
    arg1, arg2 = args
    print('arg1: %r, arg2: %r' % (arg1, arg2))


# ok that *args is actually pointlesss, we can just do this
def print_two_again(arg1, arg2):
    print('arg1: %r, arg2: %r' % (arg1, arg2))

# this just takes one argument:
def print_one(arg1):
    print('arg1: %r' % arg1)


# this one takes no argument
def print_none():
    print('I got nothing.')


print_two('Zed','Shaw')
print_two_again('Zhu', 'Xin')
print_one("First")
print_none()