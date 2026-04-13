# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:59:47 2026

@author: hudso
"""

import numpy as np
from astropy.table import Table

def main():
    x = np.linspace(0,2*np.pi,1000)
    y = np.sin(x)
    data = Table([x,y], names = ['x','sin(x)'])

    print(data)

if __name__ == '__main__':
    main()

