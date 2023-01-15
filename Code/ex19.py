#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:55:28 2018

@author: xin
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print('You have %d cheese' % cheese_count) # %d 用来显示整数数字，格式化输出使用 %
    print('You have %d boxes of crackers!' % boxes_of_crackers)
    print("Man that's enouth for a party")
    print("Get a blanket. \n")

# 简单的常量数值
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# 变量
print("OR, we can use variables from our scripts:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 常量运算结果
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 常量+变量的运算结果
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 1000, amount_of_crackers + 1000)

