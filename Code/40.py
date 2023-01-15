# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation

class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_song(self):
        for line in self.lyrics:
            print line

happy_bday = song(["Happy birthday to you", "I don't want to get sued", "so I'll stop right there"])

bulls_on_parade = song(["They rally around the family","with pockets full of shells"])

new_song = song("this is a test")
new_song1 = song(["this is a test"])


happy_bday.sing_me_song()

bulls_on_parade.sing_me_song()

new_song.sing_me_song()
new_song1.sing_me_song()
