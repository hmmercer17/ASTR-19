# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:09:19 2026

@author: hudso
"""

def f(x):
    return x**3+8


def main():
    result = f(9)
    print(result)
    
    if result > 27:
        print("YAY!")
        
if __name__ == "__main__":
    main()
    