# -*- coding: utf-8 -*-
# ex16.py


filename = 'test.txt'
target = open(filename, 'w')

line1 = "This is the first line"
line2 = "This is the second line"
line3 = "This is the third line"


print('Now I\'m going to write these three lines into the file')
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print('and finanly, we close it.')
target.close