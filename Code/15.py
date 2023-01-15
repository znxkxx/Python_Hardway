
# -*- coding: utf-8 -*-


from sys import argv

script, filename = argv
prompt = '>'

print "your file is: %s" % filename

txt = open(filename)  # open()返回的是file object
print txt.read()   # read()返回的是文件中的内容，以string形式返回
#
# file_again = raw_input('Input the file name again: ')
# txt_again = open(file_again)
# print txt_again.read()

txt.close() # 注意关闭文件的正确方式
txt_again.close()
