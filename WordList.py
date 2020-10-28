#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:07:56 2020

@author: emilyyemington
"""

import random

class WordList:
    
    def __init__(self, in_wlist):
        
        text = in_wlist.read()
        
        in_wlist.close()
        
        self.wlist = text.split("\n")
        
        templist = []
        
        for x in range(len(self.wlist)):
            templist.append(Word(self.wlist[x]))
            
        self.wlist = templist
        random.shuffle(self.wlist)
        
    def shuffle(self):
        
        random.shuffle(self.wlist)
    
    def contains(self, in_word):
        
        for word in self.wlist:
            if word.get_word() == in_word.get_word():
                print("I found the word")
                return True
        return False
    
    def find_word(self, needed_word):
        
        syl = needed_word.get_syl()
        
        if syl[0].isalpha():
            return self.get_init_letter_word(syl)
        elif syl[0] == "*" or syl[0] == "/":
            return self.get_metered_word(needed_word)
        else: 
            return self.get_syl_word(len(syl))
    
    def matching_meters(self, empty_word):
        
        out_list = []
        
        for word in self.wlist:
            if word.compare_meter(empty_word):
                out_list.append(word)
        
        random.shuffle(out_list)
        return out_list
    
    def get_metered_word(self, empty_word):
        
        m_list = self.matching_meters(empty_word)
        
        if len(m_list)==0:
            return False
        else:
            return m_list[0]
            
    def get_syl_word(self, no_syl):
        
        self.shuffle()
        for word in self.wlist:
            if word.compare_no_syl(no_syl):
                return word
        return False
    
    def matching_syls(self, no_syl):
        
        out_list = []
        
        for word in self.wlist:
            if word.compare_no_syl(no_syl):
                out_list.append(word)
        random.shuffle(out_list)
        return out_list
    
    def matching_initials(self, in_letter):
        
        out_list = []
        
        for word in self.wlist:
            if word.check_first_letter(in_letter):
                out_list.append(word)
                
        random.shuffle(out_list)
        return out_list
    
    def get_rhyming_word(self, need_word, past_word):
        
        m_list = self.matching_meters(need_word)
        
        last_syl = 4
        past_word_bol = False
        
        while last_syl > 2:
            for w in m_list:
                if w.get_word() == past_word.get_word():
                    past_word_bol = True
                    continue
                elif w.compare_rhyme(past_word, last_syl):
                    return w
            last_syl -= 1
        
        if past_word_bol:
            return past_word
        else:
            return False
        
    def get_init_letter_word(self, in_syl):
        
        print("GETINITLETWL: I recieved %s"%in_syl)
        
        in_letter = in_syl[0]
        
        print("I'm looking for a word beginning with %s"%in_letter)
        
        if in_syl.find("*") > -1 or in_syl.find("/") > -1:
            m_list = self.matching_meters(Word(in_syl))
            for w in m_list:
                if w.check_first_letter(in_letter):
                    print("I found the word %s"%w.get_word())
                    return w
        elif in_syl.find("~") > -1:
            print("I'm checking for a syl word (INIT LETTER WL)")
            s_list = self.matching_syls(len(in_syl))
            for w in s_list:
                if w.check_first_letter(in_letter):
                    print("I found the word %s"%w.get_word())
                    return w
        else:
            return self.matching_initials(in_letter)[0]
        
                
        return Word("MISTAKE: syl is %s"%in_syl)
    
            
    def get_any_word(self):
        return self.wlist[random.randint(0,len(self.wlist)-1)]
    
    def get_no_words(self):
        return len(self.wlist)
    
        
class Word:
    
    def __init__(self, in_word):
        
        if in_word.find(" ") > -1:
            wordl = in_word.split(" ")
            self.word = wordl[0]
            self.syl = wordl[1]
            self.syl = self.syl.replace("x", "*")
            self.word = self.word.replace("-", " ")
                
        elif in_word.find("*") + in_word.find("/") + in_word.find("~") + in_word.find("$")> -4:
            self.word = ""
            self.syl = in_word
        else:
            self.word = in_word
            self.syl = "*"
            
    def __str__(self):
        return self.word

    def compare_meter(self, other_word):
        if other_word.get_syl().find("~")>-1:
            return self.compare_no_syl(len(other_word.get_syl()))
        elif other_word.get_syl() == "/":
            return self.compare_no_syl(len(other_word.get_syl()))
        elif other_word.get_syl().find("/*/") > -1:
            poss1 = other_word.get_syl().replace("/*/","**/")
            poss2 = other_word.get_syl().replace("/*/","/**")
            return self.syl == other_word.get_syl() or self.syl == poss1 or self.syl == poss2 
        elif other_word.get_syl() == "**":
            return self.syl == other_word.get_syl() or self.syl in ["*/","/*"] 
        else:
            return self.compare_no_syl(len(other_word.get_syl())) and self.syl == other_word.get_syl()
        
    def compare_no_syl(self, other_syl):
        return len(self.syl) == other_syl
    
    def compare_rhyme(self, other_word, no_syl_match = 3):
        
        oth_len = len(other_word.get_word())
        oth_word = other_word.get_word()
        
        if oth_len < no_syl_match or len(self.word) < no_syl_match:
            return oth_word == self.word[0:len(oth_word)] or oth_word[0:len(self.word)] == self.word
        else:
            return oth_word[oth_len - no_syl_match:oth_len] == self.word[len(self.word) - no_syl_match : len(self.word)]
        
    def check_first_letter(self, in_letter):
        return self.get_first_letter() == in_letter
        
    def get_first_letter(self):
        return self.word[0]
    
    def get_word(self):
        return self.word
    
    def get_syl(self):
        return self.syl
    
    def pluralize_noun(self):
        
        out_word = self
        
        if self.get_word()[len(self.get_word())-1] in ["y", "i"]:
            out_word = Word(self.word[0:len(self.word)-1] + "ies " + self.syl)
        elif self.word[len(self.word)-2: len(self.word)] in ["is"]:
            out_word = Word(self.word[0:len(self.word)-2] +"es " + self.syl)
        else:
            out_word = Word(self.word +"s " + self.syl)
            
        return out_word

    
