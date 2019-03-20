# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:44:12 2018

@author: Stärkie
"""
import pandas as pd
from io import StringIO

class Series(object):
    """
    Class for storing a measurement series in the form of multiple measurement
    objects.
    """
    def __init__(self):
        """
        On creation this method initializes a empty series.
        """
        self.series = []
        self.current = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.series)-1:
            self.current += 1
            return self.series[self.current]
        else:
            self.current = -1
            raise StopIteration
    
    def append(self, measurement):
        """
        Append a measurement.
        """
        self.series.append(measurement)
        
class Csv_params(object):
    """
    Class representing the characteristics of a csv file.
    """
    def __init__(self, sep='\t', dec='.', skiprows=1, names=['x', 'y']):
        """
        On creation: give the value separator sep, the decimal point character
        dec and the number of rows to skip.
        """
        self.sep = sep
        self.dec = dec
        self.skiprows = skiprows
        self.names = names
        
class Measurement(object):
    """
    Class representing a measurement (aka one dataframe containing the data of
    a single csv file).
    """
    def __init__(self, f, csv_params):
        """
        To create this object give a Csv_params object to specify the params of
        the given csv file format.
        """
        self.csvp = csv_params
        self.update(f, self.csvp)
        
    def update(self, f, csv_params):
        """
        This method (re)creates the dataframe using the csv_params.
        """
        with open(f, 'r') as f: 
            txt = f.read()
        print(txt[:100])
        txt = txt.replace(csv_params.dec, '.')
        print(txt[:100])
        self.df = pd.read_csv(StringIO(txt), sep=csv_params.sep, 
                              skiprows=csv_params.skiprows,
                              names=csv_params.names)
        
