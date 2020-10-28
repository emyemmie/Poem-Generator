 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:20:36 2020

@author: emilyyemington
"""
import Author as AuthClass
import Poems as P
import Helper as HP
import meters as Meters
import WordList as WL

sorry = "Sorry, I don't understand. Please try again"

files = [open("defnoun.txt"),open("defverb.txt"),open("defadj.txt"),open("defarts.txt"), open("defcon.txt")]
wls = []

for x in files:
    wls.append(WL.WordList(x))
    
dictionary = {"Nouns" : wls[0], "Verbs" : wls[1], "Adjectives" : wls[2], "Articles" : wls[3], "Conjunctions" : wls[4]}

vocab = AuthClass.Vocabulary(wls[0], wls[1], wls[2], wls[3], wls[4])

print("\nHello, poet! What's your name?")
name = input()

print("\nOkay, %s, let's start with the basics: what do you want to call your poem?" %name)
title = input()
if title == "random":
    vocab.get_word("~", 2) + " " + vocab.get_word("~", 0)

print("\nWonderful! Now, what kind of poem are you looking to write? Your options are:\n")

poemTypes = {0:"Sonnet", 1:"Villanelle", 2: "Ballad", 3: "Haiku", 4: "Acrostic", 5: "Free Verse", 6: "Advanced"}

count = 0

while count < len(poemTypes):
    print("%d: %s"%(count,poemTypes[count]))
    count += 1

print("\nType in the number of the type of poem you want to write:")

type1 = int(input())
typeTrans = poemTypes[type1]

if typeTrans != "Advanced":
    print("\nA %s? Good choice!"%typeTrans)
else:
    print("\nWonderful! Let's get started.")
    
help_bot = HP.Helper()

print("\nHow many poems would you like to write?")
numpoems = int(input())

#poem_type = help_bot.initiate_poem(type1)

auth = AuthClass.Author(vocab, name)


poem_type = help_bot.initiate_poem(type1, numpoems)

for x in range(numpoems):
    my_poem = auth.write_poem(title, poem_type[x])
    my_poem.print_poem(title, name)
    