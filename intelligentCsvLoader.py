# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 19:42:32 2018

@author: Stärkie
"""

import datautil
import operator
import clinterface as ci
import glob
import os
import pickle as pkl

def data_loader(search_string):
    """
    Main method. Use this to (re-)load a series of csv-files matching the regex
    search_string.
    returns: a Series object containing a list of measurement objects and a 
    Csv_params object describing the csv file. 
    """
    if os.path.isfile(f'pythonsaves/{name_from_search(search_string)}_series.pkl'):
        ci.print_head('Found a previous save, loading...')
        csvp, series = load_series(name_from_search(search_string))
    else:
        sample_file = glob.glob(search_string)[0] # Catch error
        csvp, series = create_series(sample_file, search_string)
    return csvp, series

def create_series(sample_file, search_str):
    """
    Main method for creating a measurment series. Specify a sample file and a 
    search string and the program will autoload the csv_files matching the
    search string.
    """
    # Detect and correct csv format
    with open(sample_file, 'r') as f: txt = f.read()
    ci.show_txt(txt)
    sep, dec = autodetect_format(txt)
    print(f'I autodetected a value separator: {sep} and a decimal point character {dec}')
    # Todo: Maybe add a view of the dataframe as it is currently detected
    while not ci.query_yes_no('Is this correct?'):
        sep, dec = format_by_hand()
    skiprows, names = set_skiprows_and_title()
    
    csvp = datautil.Csv_params(sep=sep, dec=dec, skiprows=skiprows, names=names)
    m = datautil.Measurement(sample_file, csvp)
    ci.display_df(m.df)
    
    # Detect and correct files matching the search string
    files = search_files(search_str)
    while not ci.query_yes_no('Are those all the files (and no more) that you wanted?'):
        search_str = input('New search string:')
        files = search_files()
    
    # create series
    series = datautil.Series()
    for f in files:
        m = datautil.Measurement(f, csvp)
        series.append(m)
        print(f'Successfully loaded the file {f} using the specified parameters.')
        
    # Save everything
    ci.print_head('Saving everything...')
    if not os.path.isdir('pythonsaves'):
        os.mkdir('pythonsaves')
    os.chdir('pythonsaves')
    name = name_from_search(search_str)  # remove * from regex
    pickler(series, f'{name}_series.pkl')
    pickler(csvp, f'{name}_csv_params.pkl')
    os.chdir('..')
    ci.print_head('Printed the saves')
    return csvp, series
    
def load_series(series_name): #to load already read series in pkl format
    """
    This method is called to reload a series that has already been created. The
    method is
    """
    os.chdir('pythonsaves')
    with open(f'{series_name}_csv_params.pkl', 'rb') as csvpf:
        csvp = pkl.load(csvpf)
    csvpf.close()
    with open(f'{series_name}_series.pkl', 'rb') as seriesf:
        series = pkl.load(seriesf)
        
    os.chdir('..')
    return csvp, series

def name_from_search(search_str):
    """
    This method is used to assign a specific search string a unique series 
    name in order to identify the series when reloading it. Currently the 
    method only strips the * character from the search string. In the future
    this method should also filter out all other regex characters.
    """
    return search_str.replace('*', '')
    
def pickler(obj, name):
    """
    This method is responsible for storing python objects in a manner so that 
    they can be reloaded later on.
    """
    with open(name, 'wb') as f:
        pkl.dump(obj, f)
    f.close()

def autodetect_format(txt):
    """
    Try and guess which character is the delimiter and which is the decimal
    place holder. Currently looking for commas, semicolons, dots and tabs.
    """
    delims = {}
    delims[','] = txt.count(',')
    delims[';'] = txt.count(';')
    delims['.'] = txt.count('.')
    delims['\t'] = txt.count('\t')
    
    sorted_delims = sorted(delims.items(), key=operator.itemgetter(1))
    sep = (sorted_delims[-2])[0]
    dec = (sorted_delims[-1])[0]
    return sep, dec

def set_skiprows_and_title():
    skiprows = int(input('How many rows do you want to skip?'))
    names = input('Specify column names separated by , :').split(',')
    return skiprows, names

def format_by_hand():
    sep = input('Specify value separator character:')
    dec = input('Specify the decimal point character:')
    return sep, dec

def search_files(search):
    files = []
    ci.print_head('Found the following files matching the search params')
    for f in glob.glob(search):
        print(f)
        files.append(f)
    return files