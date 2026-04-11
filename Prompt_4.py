# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:23:19 2026

@author: hudso
"""


class SeaOtter:
    def print(self):
        print('Characteristics of a Sea Otter:')
        print(f'Arm Length: {self.arm_len}')
        print(f'Leg Length: {self.leg_len}')
        print(f'Number of Eyes: {self.num_eyes}')
        print(f'Tail?: {self.tail}')
        print(f'Furry?: {self.furry}')
        
        
    def __init__(self, arm_len, leg_len, num_eyes, tail, furry):
        self.arm_len = arm_len
        self.leg_len = leg_len
        self.num_eyes = num_eyes
        self.tail = tail
        self.furry = furry
   
        
test = SeaOtter(arm_len = 1.1, leg_len = 3.2, num_eyes = 2, tail = True, furry = True)

test.print()

