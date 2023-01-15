# -*- coding: utf-8 -*-

from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n-----------"
            next_sene_name = current_scene.enter()


class Death(Scene):
    quips = [
        "you died. you kinda suck at this.",
        "your mom would be proud...if she were smarter.",
        "Such a loser",
        "I have a small pupyy that's better at this"
    ]

    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed "
        print "your entire crew. You are the last surviving member and your last mission "
        print "is to get your netroan destruct bomb from the weapon Armory, "
        print "put it in the bridge, and blow the ship up after geting into an escape pod. "
        print "\n"

        print "You are running down the central corridor to the Weapons Armoy when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "following around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        
    action = raw_input("> ")
    
    if action == "shoot!":
        print "Quick on the draw you yank out your blaster and fire it at the Gothon "
        print "His clown costume is flowing and moving around his body, which throws "
        print "off your aim. Your laser hits his costume but misses him entirely. This "
        print "completely ruins his brand new costume his mother bought him, which makes "
        print "him fly into a rage and blast you repeatedly in the face until you are "
        print "dead. Then he eats you."
        
        return 'death'
        
    elif action == "dodge!":
        print "Like a world class boxer you dodge, weave, slip and slide right as the "
        print "Gothon's blaster cranks a laser past your head."
        print "In the middle of your artful dodge your foot slips and you bang your head "
        print "on the metal wall and pass out. You wake up shortly after only to die "
        print "as the Gothon stomps on your head and eats you."
        
        return 'death'
        
    elif action == "tell a joke":
        print "Lucky for you they made you learn Gothon insults in the academy. You tell "
        print "the one Gothon joke you know:"
        print "Lbhe zbgure vf fb sng, jura adjfi djf dkfji djdgg."
        print "The Gothon stops, tries not to laugh, then busts out laughing and can't move. "
        print "While he's laughing you run up and shoot him square in the head putting "
        print "him down, then jump through the Weapon Armory door."
        
        return 'laser_weapon_armory'
    
    else:
        print "DOES NOT COMPUTE!"
        return 'central_corridor'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
