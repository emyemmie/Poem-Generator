#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:33:59 2020

@author: emilyyemington
"""

class Meter:
    
    def __init__(self):
        
        self.pattern = "~"
    
    def get_pattern(self):
        
        return self.pattern
    
    def get_meter_line(self, in_syl):
        
        line = ""
        
        if in_syl > len(self.pattern):
            line += self.pattern * (in_syl//len(self.pattern))
            
        end = int(in_syl%len(self.pattern))
        
        line += self.pattern[0:end]
        
        return line
        
    def get_meter_poem(self, in_syl, in_lines):
        
        count = 0
        poem = []
        
        while count < in_lines:
            poem.append(self.get_meter_line(in_syl))
            count += 1
        
        return poem
    
class Iambic(Meter):
    
    def __init__(self):
        
        self.pattern = "*/"
    
class Trochaic(Meter):
    
    def __init__(self):
        
        self.pattern = "/*"
        
class Anapestic(Meter):
    
    def __init__(self):
        
        self.pattern = "**/"
        
class Dactylic(Meter):
    
    def __init__(self):
        
        self.pattern = "/**"