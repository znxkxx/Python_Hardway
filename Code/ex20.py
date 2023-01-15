#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ex20.py

# 定义一个函数，用于打印输出文件的内容
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, ":", f.readline())


current_file = open("test.txt")

print("First let's print the whole file:\n")
print_all(current_file)


print("Now let's rewind, kind of like a tape.")
rewind(current_file) # don't konw how this work? or what's the function of rewind()?


print("Let's print the two lines:")
current_line = 1
print_a_line(current_line,current_file)

#
# current_line = current_line + 1
# print_a_line(current_line,current_file)
#
# current_line = current_line + 1
# print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)


current_line -= 1
print_a_line(current_line,current_file)