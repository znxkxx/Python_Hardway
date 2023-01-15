# -*- coding: utf-8 -*-
# ex15.py

from sys import argv

txt = open(filename)

print('Here is your file: %r' %filename)
print(txt.read())


print('Type the filename again:')
file_again = input('> ')

txt_again = open(file_again)
print txt_again.read()