# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 19:55:49 2018

@author: Stärkie
"""
import sys

def show_txt(txt, name='Sample file'):
    """
    Display a txt, such as the raw csv file to let user view the format.
    """
    print_head(name)
    lines = txt.split('\n')
    if len(lines) > 10:
        print('\n'.join(lines[:10]))
    else: print(lines)
    
def print_head(title):
    """
    Print pretty nice looking title of something.
    """
    if len(title) < 66 :
        titlesep = int((66 - len(title))/2)
    else: titlesep = 0
    print('-'*66)
    print(' '*titlesep + f'{title}' + ' '*titlesep)
    print('-'*66)
    
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
            
def display_menu(title, options):
    if len(title) < 66 :
        titlesep = int((66 - len(title))/2)
    else: titlesep = 0
    print('-'*66)
    print(' '*titlesep + f'{title}' + ' '*titlesep)
    for i, option in enumerate(options):
        print(f'{i}) {option}')
    print('-'*66)
    try:
        menint = input('Chose the action: ')
        return int(menint)
    except KeyError:
        print('Please choose one of the inputs (via 1, 2, 3, ...)')
        display_menu(title, options)
        
def display_df(df):
    print_head('Current Dataframe')
    print(df.head(10))
    print('...')
    print_head('Stats of the dataframe:')
    print(df.describe())
    print('='*66)