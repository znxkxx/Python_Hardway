print "test1 start here:"
print "------------------------"
elements = []
for i in range(6):
    print "adding %d to the list" % i
    elements.append(i)
for i in elements:
    print "Elemet was %d" % i

print "------------------------"
print "test1 end here:"


print "test2 start here:"
print "------------------------"
elements = range(6)

for i in elements:
    print "Elemet was %d" % i
print "------------------------"
print "test2 end here:"
