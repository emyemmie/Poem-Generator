#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:34:45 2020

@author: emilyyemington
"""

import random
import meters
import WordList as WL

class Poem:
    
    def __init__(self, in_rhythm, in_lines = [], in_poss = []):
        self.rhythm = in_rhythm
        self.lines = [[]*len(in_rhythm)]
        self.poss = in_poss
        self.rhymes = False
        
    def set_rhythm(self, in_rhythm):
        self.rhythm = in_rhythm

    def get_rhythm(self):
        return self.rhythm
    
    def get_line(self, line):
        return self.rhythm[line]
    
    def no_lines(self):
        return len(self.rhythm)
    
    def add_word(self, in_word, in_line):
        
        self.lines[in_line].append(in_word) 
    
    def add_line(self):
        
        self.lines.append([])
    
    def add_poss(self, in_pos):
        
        self.poss.append(in_pos)
    
    def get_poss(self):
        
        return self.poss
    
    def get_last_pos(self):
        
        return self.poss[len(self.poss)-1]
    
    def no_lines_written(self):
        
        return len(self.lines)
    
    def get_last_word(self):
        
        writ = self.no_lines_written()
        ind_line = len(self.lines[writ-1])
        
        if ind_line > 0 and writ > 0:
            return WL.Word("GOAHEAD")
        else:
            return self.lines[writ - 1][ind_line - 1]
        
    def get_last_word_of_line(self, in_line): #returns a Word object of last line
        
        line = self.lines[in_line]
        word = line[len(line)-1]
        if word.get_word() == "." or word.get_word() == ",":
            word = line[len(line)-2]
        return word
    
    def it_rhymes(self):
        self.rhymes = True
    
    def does_it_rhyme(self):
        
        return self.rhymes
        
    def print_poem(self, in_title, in_name):
        
        print("\n%s:\n%s by %s\n"%(in_title, self.ptype(),in_name))
        
        for line in self.lines:
            line_text = ""
            count = 0
            while count < len(line):
                word = line[count]
                if word.get_word() == "." or word.get_word() == ",":
                    line_text = line_text[0:len(line_text)-1]
                elif count > 0 and word.get_word()[0] in ["a", "e", "i","o","u"] and line[count-1].get_word() == "a":
                    line_text = line_text[0: len(line_text)-1] + "n "
                line_text = line_text + word.get_word() + " "
                count += 1
            print("\n%s"%line_text)
    
class RhymedPoem(Poem):
    
    def __init__(self, in_scheme):
        self.scheme = in_scheme
        super().it_rhymes()
        
    def get_scheme(self):
        return self.scheme
    
    def get_line_scheme(self,in_line):
        return self.scheme[in_line]
    
    def get_last_rhyme_line(self, in_line, in_rhyme): #returns line of last rhyme or -1 if none
        
        in_let = in_rhyme
        
        if len(in_let) > 1:
            if in_line == 0:
                return -1
            for x in self.scheme[0 : in_line]:
                if in_let == x:
                    return self.scheme.index(x) # returns line 
            return -1
        elif len(in_let) == 1:
            if in_let == "~":
                return -1
            else:
                if in_line == 0:
                    return -1
                else:
                    for let in self.scheme[0 : in_line]:
                        if let == in_let:
                            print(self.scheme.index(let))
                            return self.scheme.index(let)
                    return -1
                
        else:
            return -1

class StrictMeteredPoem(Poem):
    
    def __init__(self, in_no_line, in_no_syl, in_meter):
        Poem.__init__(self,in_meter.get_meter_poem(in_no_syl, in_no_line))
        self.meter = in_meter
        
    def ptype(self):
        
        return ("An Advanced Poem")
    
    def get_meter(self):
        
        return self.meter
        
class Sonnet(StrictMeteredPoem, RhymedPoem):
    
    def __init__(self):
        
        scheme = ["A","B","A","B","C","D","C","D","E","F","E","F","G","G"]
        
        StrictMeteredPoem.__init__(self, 14, 10, meters.Iambic())
        RhymedPoem.__init__(self,scheme)
    
    def ptype(self):
    
        return "A Sonnet"
        
class Villanelle(StrictMeteredPoem, RhymedPoem):
 
    def __init__(self):
        
        scheme = ["A1", "B", "A2", "A", "B", "A1", "A", "B", "A2", "A", "B", "A1", "A", "B", "A2", "A", "B", "A1", "A2"]
        
        StrictMeteredPoem.__init__(self,19, 10, meters.Iambic())
        RhymedPoem.__init__(self, scheme)
        
    def ptype(self):
    
        return "A Villanelle"
        
class StrangeMeteredPoem(Poem):
    
    def __init__(self, in_pattern, in_meter):
        
        super().__init__([])
        
        self.rhythm = []        
        
        for line in in_pattern:
            self.rhythm.append(in_meter.get_meter_line(line))
            
        self.lines = [[]*len(self.rhythm)]
        self.poss = []
        self.meter = in_meter
        
    def get_meter(self):
        
        return self.meter
    
    def ptype(self):
        
        return ("An Advanced Poem")
        
        
class Ballad(StrangeMeteredPoem, RhymedPoem):
    
    def __init__(self):
        
        scheme = ["-", "A", "-", "A", "-", "B", "-", "B", "-", "C", "-", "C", "-", "D", "-", "D"]
        
        super().__init__([8,6,8,6,8,6,8,6,8,6,8,6,8,6,8,6], meters.Iambic())
        
        RhymedPoem.__init__(self,scheme)
        
    def ptype(self):
    
        return "A Ballad"

class Haiku(Poem):
    
    def __init__(self):
        super().__init__(["$$$$$", "$$$$$$$", "$$$$$"])
        
    def ptype(self):
    
        return "A Haiku"
        
class FreeVerse(Poem):
    
    def __init__(self):
        self.rhythm = []
        
        for x in range(random.randint(1,15)):
            self.rhythm.append("~"*random.randint(1,10))
            
        self.lines = [[]*len(self.rhythm)]
        self.poss = []
        self.rhymes = False
        
    def ptype(self):
    
        return "A Free Verse Poem"

class Acrostic(FreeVerse):
    
    def __init__(self, in_word):
        
        self.rhythm = []
        in_word = in_word.lower()
        
        for x in range(len(in_word)):
            self.rhythm.append(in_word[x]+"~"*random.randint(1,9))
        
        self.lines = [[]*len(in_word)]
        
        Poem.__init__(self,self.rhythm, self.lines)
        
    def ptype(self):
        
        return "An Acrostic Poem"
        
