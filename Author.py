#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:03:28 2020

@author: emilyyemington
"""
import random
import Poems
import WordList as WL
import meters

print("reloaded Author.py")

class Author:
    
    def __init__(self, in_vocabulary, in_name = "Anonymous"):
        
        self.name = in_name
        self.vocab = in_vocabulary
        self.works = {}
        
    def get_name(self):
        
        return self.name
    
    def write_poem(self, in_title, in_poem = Poems.FreeVerse()):
        
        if in_title == "\n":
            title = self.vocab.get_any_word(0).get_word()
        else:
            title = in_title
        
        poem = in_poem
        
        x = 0
        
        while x < in_poem.no_lines():
            
            mini_rhy = in_poem.get_line(x)
            
            while len(mini_rhy)>0:
                
                pos = 0
                
                no_syl_left = len(mini_rhy)
                
                #print("the length of poss is %s"%len(poem.get_poss()))
                
                if mini_rhy[0].isalpha():
                    pos = random.randint(0,2)
                elif len(poem.get_poss()) == 0:
                    pos = random.randint(0,4)
                else:
                    pos = self.get_next_pos(poem)
                
               #print("I'm looking for pos %d"%pos)
                
                some_syl = 0
                
                
                #print("mini_rhy 0 is %s"%mini_rhy[0])
                if pos == 3 or mini_rhy[0]=="~" or mini_rhy[0].isalpha():
                    some_syl = 1
                else:
                    while isinstance(poem, Poems.StrangeMeteredPoem) or isinstance(poem, Poems.StrictMeteredPoem) or isinstance(poem, Poems.Haiku):
                        some_syl = self.get_no_syl_by_percent()
                        #print("I've decided on %d syllables"%some_syl)
                        
                        if type(poem) == Poems.Haiku or (some_syl <= no_syl_left and poem.get_meter() not in [type(meters.Anapestic()), type(meters.Dactylic())]):
                            break
                        elif some_syl <= no_syl_left and poem.get_meter() in [type(meters.Anapestic()), type(meters.Dactylic())] and some_syl<4:
                            break
                
                out_syl = mini_rhy[0:some_syl]
                #print("I want" + out_syl)
                
                #print("I'm looking for syllables %s"%out_syl)
                
                got_word = ""
                
                if poem.does_it_rhyme() and len(out_syl) == len(mini_rhy):
                    
                    #print("I need to rhyme")
                    
                    if pos in [3,4]:
                        pos = self.get_next_pos(poem, [0,1,2])
                        #print("set pos to %s"%pos)
                    
                    curr_rhyme = poem.get_line_scheme(x) #the line rhyme we have now
                    #print(curr_rhyme)
                    last_rhyme = poem.get_last_rhyme_line(x, curr_rhyme) #int of last line with rhyme
                    #print("the last line this rhymed was %s"%last_rhyme)
                    if last_rhyme == -1:
                        got_word = self.vocab.get_word(out_syl, pos)
                        #print("ignore")
                    elif len(curr_rhyme) > 1:
                        got_word = poem.get_last_word_of_line(last_rhyme) #sets equal to last word if formal A1, for ex
                        #print("THE WORD I NEED TO REPEAT IS %s"%got_word.get_word())
                        pos = self.vocab.find_pos_of_word(got_word)
                        #print("Found pos of word to be %s"%pos)
                    else:
                        rhyming_word = poem.get_last_word_of_line(last_rhyme)
                        #print("I need to rhyme %s"%rhyming_word)
                        
                        got_word = self.vocab.get_rhyming_word(out_syl, rhyming_word, pos)
                                
                        while got_word == False:
                            for j in range(100):
                                pos = self.get_next_pos(poem)
                                #print("TRY: POS IS %s"%pos)
                                got_word = self.vocab.get_rhyming_word(out_syl, rhyming_word, pos)
                                if got_word == False:
                                    continue
                                else:
                                    break
                            if got_word == False:
                                #print("\t\tI gave up")
                                got_word = self.vocab.get_word(out_syl, pos)
                            #else:
                                #print("I rhymed %s with %s"%(got_word.get_word(), poem.get_last_word_of_line(last_rhyme).get_word()))
                
                else:
                    #print("out_syl is %s"%out_syl)
                    got_word = self.vocab.get_word(out_syl, pos)
                    #print("I got the word: %s"%got_word)
                    
                poem.add_poss(pos)
                #print("added pos %s"%pos)
                
#                if pos == 0:
#                    plur = random.randint(0,1)
#                    if plur == 0 and poem.get_last_word().get_word() not in ["that", "a", "who"]:
#                        got_word = got_word.pluralize_noun()
                
                if type(got_word) is WL.Word:
                    mini_rhy = mini_rhy[len(got_word.get_syl()):len(mini_rhy)]
                    poem.add_word(got_word, x)
                    #print("I added the word '%s' to the poem!"%got_word.get_word())
                    punc = random.randint(0,12)
                    if poem.get_last_pos() < 3:
                        if punc == 0 or punc == 1 :
                            poem.add_word(WL.Word(","), x)
                        elif punc == 2:
                            poem.add_word(WL.Word("."), x)
                else:
                    mini_rhy = mini_rhy
                
            poem.add_line()
            #print("\nnew line!")
            x = x + 1
                

        self.works[title] = poem
        
        return poem
            
        
    def get_previous_works(self):
        
        return self.works
    
    def get_no_syl_by_percent(self):
        
        no = random.randint(0,97)
        
        if no < 30:
            return 1
        elif no < 66:
            return 2
        elif no < 85:
            return 3
        else:
            return 4
    
    def get_next_pos(self, in_poem, in_range = [0,1,2,3,4]): #VERY RUDIMENTARY
        
        pos = in_poem.get_last_pos()
        #print("the last pos was %d"%pos)
        choices = in_range
        new_choices = []
        
        for x in choices:
            if x == pos:
                continue
            else:
                new_choices.append(x)
        
        #print("my choices are %s"%new_choices)
        
        return random.choice(new_choices)
    
    def think_of_title(self):
        return "The " + self.vocab.get_word("~", 2) + " " + self.vocab.get_word("~", 0)
    
class Vocabulary:
    
    def __init__(self, in_n, in_v, in_adj, in_art, in_con):
        
        self.noun = in_n
        self.verb = in_v
        self.adj = in_adj
        self.art = in_art
        self.con = in_con
        self.list_parts = [self.noun, self.verb, self.adj, self.art, self.con]
        self.dct = {}
        
        for x in range(len(self.list_parts)):
            self.dct.update({self.list_parts[x]:x})
        
        
    def get_word(self, in_syll, in_pos = random.randint(0,4)):
        
        #print("there are %d syllables"%len(in_syll))
        
        in_word = WL.Word(in_syll)
        #print("get_word received %s"%in_word.get_syl())
        out_word = ""
        
        if in_syll[0].isalpha():
            #print("authorletter")
            #print("GETWORD: I should be looking for an init letter")
            if not in_pos == 3:
                #print("GETWORD: I'm sending getinitwordvocab in_syll %s"%in_syll)
                out_word = self.get_init_letter_word(in_syll, in_pos)
            else:
                out_word = self.get_init_letter_word(in_word.get_syl(), random.randint(0,2)) #CHANGE
        elif in_word.get_syl()[0] == "~":
            #print("author~")
            out_word = self.get_any_word(in_pos)
        elif in_word.get_syl()[0] == "*" or in_word.get_syl()[0] == "/":
            #print("author*/")
            out_word = self.get_metered_word(in_word, in_pos)
        elif in_word.get_syl()[0] == "$": 
            #print("author$")
            #print("I'm finding a word with %d syllables"%len(in_syll))
            out_word = self.get_syl_word(len(in_syll), in_pos)
        else:
            #print("authorelse")
            out_word = self.list_parts[in_pos].get_any_word()
    
        return out_word


    def get_rhyming_word(self, in_syl, in_past, in_pos = random.randint(0,4)):
        
        return self.list_parts[in_pos].get_rhyming_word(WL.Word(in_syl), in_past)

    def get_any_word(self, in_pos = random.randint(0,4)):
        
        return self.list_parts[in_pos].get_any_word()
    
    def get_syl_word(self, no_syl, in_pos = random.randint(0,4)):
        
        out_word = self.list_parts[in_pos].get_syl_word(no_syl)
        
        return out_word
    
    def get_metered_word(self, empty_word, in_pos = random.randint(0,4)): #can be reduced to one line once debugging is over
        
        out_word = self.list_parts[in_pos].get_metered_word(empty_word)

        return out_word
    
    def get_init_letter_word(self, in_syl, in_pos = random.randint(0,2)):
        
        pos = in_pos
        
        if pos == 3:
            pos = random.randint(0,2)
        
        
        #print("AUTH: I'm sending WL %s in list %s"%(in_syl, pos))
        out_word = self.list_parts[pos].get_init_letter_word(in_syl)
        
        return out_word
    
    def find_pos_of_word(self, in_word):
        
        for wl in self.list_parts:
            #print("I'm looking for the word %s in list %s"%(in_word.get_word(), wl))
            try:
                if wl.contains(in_word):
                    #print("wl object is %s"%wl)
                    return self.dct.get(wl)
            except:
                continue
                
    
            