# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation

state = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Deroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = "New York"
cities['OR'] = "Portland"

# print out some cities
print '--' * 20  # 连续输出10个短横线
print 'NY State has: ', cities['NY']
print "OR State has: ", cities['OR']
