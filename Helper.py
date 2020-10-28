#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:11:42 2020

@author: emilyyemington
"""

import meters as Meters
import Poems as P

class Helper:
    
    def __init__(self):
        
        self.name = "Help Bot"
        self.sorry = "\nSorry, I don't understand. Please try again:"
        
    def say_hello(self):
        
        print("Hi! I'm %s."%self.name)
        
    def check_int(self, in_str, limit = 100):

        if in_str.isdigit() and int(in_str) in range(limit + 1):
            return True
        else:
            return False
        
    def get_meter(self, in_meter_dict, in_key):
        
        if in_meter_dict[in_key] == "Iambic":
            return Meters.Iambic()
        elif in_meter_dict[in_key] == "Trochaic":
            return Meters.Trochaic()
        elif in_meter_dict[in_key] == "Anapestic":
            return Meters.Anapestic()
        elif in_meter_dict[in_key] == "Dactylic":
            return Meters.Dactylic()
            

    def initiate_poem(self,type_no, numpoems):
        
        arr = []
        
        if type_no == 0:
            
            print("\nWriting your sonnet...")
            for x in range(numpoems):
                arr.append(P.Sonnet())
                
            return arr
        
        elif type_no == 1:
            
            print("\nWriting your villanelle...")
            
            for x in range(numpoems):
                arr.append(P.Villanelle())
                
            return arr
        
        elif type_no == 2:
            
            print("\nWriting your ballad...")
            for x in range(numpoems):
                arr.append(P.Ballad())
                
            return arr
        
        elif type_no == 3:
            
            print("\nWriting your haiku...")
            for x in range(numpoems):
                arr.append(P.Haiku())
                
            return arr
        
        elif type_no == 4:
            
            print("\nNow, what word would you like to base your poem off of?")
            
            while True:
                answer = input()
                if answer.isalpha():
                    break
                else:
                    print("\nSorry, all characters must be in the alphabet. Please try again:")
            
            print("\nWriting your acrostic poem...")
            for x in range(numpoems):
                arr.append(P.Acrostic(answer))
                
            return arr
            
        elif type_no == 5:
            
            print("\nWriting your free verse poem...")
            for x in range(numpoems):
                arr.append(P.FreeVerse())
                
            return arr
        
        elif type_no == 6:
            
            meters = {0:"Iambic", 1:"Trochaic",2:"Anapestic",3:"Dactylic"}
            
            meter_choice = 0
            
            while True:
                count = 0
        
                print("\nChoose a meter:")
                
                while count < len(meters):
                    print("%d: %s"%(count,meters[count]))
                    count += 1
                
                meter_choice = input()
                
                if self.check_int(meter_choice, len(meters)):
                    meter_choice = int(meter_choice)
                    break
                else:
                    print(self.sorry)
            
            my_meter = self.get_meter(meters, meter_choice)
            
            print("\nOkay, you've chosen %s Meter. Now, type in the number of lines you'd like:"%meters[meter_choice])
            
            no_lines = 14
            
            while True:
                
                no_lines = input()
                
                if self.check_int(no_lines):
                    no_lines = int(no_lines)
                    break
                else:
                    print(self.sorry)
                    
            print("\nYou've chosen %d lines. Would you like a consistent number of syllables or would you like to change it up with each line?"%no_lines)
            
            while True:
                
                print("\n0: Consistent\n1: Inconsistent")
                
                syl_consistency = input()
                
                if self.check_int(syl_consistency, 1):
                    syl_consistency = int(syl_consistency)
                    break
                else:
                    print(self.sorry)
            
            if syl_consistency == 0:
                
                print("Phew! That makes it easier. How many syllables would you like?")
                
                while True:
                    
                    syl_no = input()
                    
                    if self.check_int(syl_no):
                        
                        syl_no = int(syl_no)
                        break
                    
                    else:
                        
                        print(self.sorry)
                        
                print("Writing your poem...")
                
                for x in range(numpoems):
                    arr.append(P.StrictMeteredPoem(no_lines,syl_no,my_meter))
            
            elif syl_consistency == 1:
                
                print("\nGreat! Please enter the number of syllables for each line one at a time:")
                
                list_syl = []
                
                for x in range(no_lines):
                    
                    while True:
                        
                        print("\nLine %d:"%x)
                        inp = input()
                        
                        if self.check_int(inp):
                        
                            list_syl.append(int(inp))
                            break
                        
                        else:
                            
                            print(self.sorry)
                
                print("\nWriting your poem...")
                
                for x in range(numpoems):
                    arr.append(P.StrangeMeteredPoem(list_syl, my_meter))
                
            return arr
                    
                    