#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ex24.py

print("Let's practice everything.")
print("You'd need to know about escapes with \\ that do \n newlines an \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is one.
"""

print("-------------------")
print(poem)
print("-------------------")

five = 10 - 2 + 3 - 6
print("This should be fie: %s" % five)  # 格式化输出 但%s应该是输出字符？


def secret_formula(started):
    # this function return three values (in list?)
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." %
      (beans, jars, crates))  # 格式化输出中，是以%分割开来。没有逗号。


start_point = start_point / 10
print("We can also do that this way:")
print("We'd like to have %d beans, %d jars , and %d crates" %
      secret_formula(start_point) ) # 函数的返回值也是在一个list中的



























