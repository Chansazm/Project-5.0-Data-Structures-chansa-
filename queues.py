#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:58:19 2019

@author: chansa
"""

class Queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self, item):
        pass
    
    def peek(self):
        pass
    
    def size(self):
        pass
    
    def is_empty(self):
        pass