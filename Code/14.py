
# -*- coding: utf-8 -*-


from sys import argv

script, username = argv
prompt = '>'


print "Hi %s， I'm the %s script." % (username, script)
print "some more questions"

print "Do you like me %s?" % (username)
likes = raw_input(prompt)



print "so you %r me" % likes
