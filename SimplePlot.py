# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:56:55 2018

@author: Stärkie
"""

import matplotlib.pyplot as plt

def plot(x, ys, xname='x', yname='y', figname='x vs. y'):
    fig, ax = plt.subplots()
    fig.set_label(figname)
    for y in ys:
        print(y)
        ax.plot(x, y)
    ax.set_xlabel(xname)
    ax.set_ylabel(yname)
    
    plt.show()
    