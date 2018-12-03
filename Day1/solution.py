#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:22:07 2018

@author: Eric Reidelbach

:DESCRIPTION:
    - Day 1 challenge 
        * https://adventofcode.com/2018/day/1
"""
 
#==============================================================================
# Package Import
#==============================================================================
import os
import pandas as pd
import pathlib

#==============================================================================
# Reference Variable Declaration
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================
def ingest_input(file_input):
    '''
    Purpose: Ingest data given a specific filename or filepath

    Input: 
        (1) file_input (string): Filename of data for part 1 challenge
    
    Output: 
        (1) NONE 
    '''
    df = pd.read_csv(file_input)
    
    return df

def increment_frequency(current, change):
    '''
    Purpose: Increment a frequency value, 'current', by the value of 'change'

    Input: 
        (1) current (int): Value of the current frequency
        (2) change (int):  Value that the frequency shall be incremented (+/-)
    
    Output: 
        (1) new (int): Value of the frequency after being incremented (+/-)
    '''
    new = current + change
    return new
    
def advance_list(idx):
    '''
    Purpose: Obtain the next value up in a list of integers. If we have reached
        the end of the list, start over.

    Input: 
        (1) idx (int): Current position in the list
    
    Output: 
        (1) new_num (int): New value by which to increment the frequency
        (2) new_idx (int): New index position in the list (either incremented
                by 1 or starting over at 0 if > than the length of the list)
    '''    
    # Check to see if we've exceeded the boundaries of the list; 
    #   If so, start over at the beginning
    if idx == len(list_freq):
        idx = 0
        
    new_num = list_freq[idx]
    new_idx = idx + 1
    
    return new_num, new_idx

def check_frequency_history(current, set_seen):
    '''
    Purpose: Determine if the current frequency equals a value that it has 
        previously reached during an earlier incrementation.

    Input: 
        (1) current (int): Value of the current frequency
        (2) set_seen (set of ints): A record of all values that a frequency
                has reached during the increment process
    
    Output: 
        (1) seen (boolean): True if the frequency has been previously achieved,
                or False if it has not
    '''
    if current in set_seen:
        print('Duplicate value found!! Duplicate frequency is: ' + str(value))
        return True, set_seen
    else:
        # Add the new value, 'current', to the list for future verification
        set_seen.add(current)
        return False, set_seen
    
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
#path_project = pathlib.Path(__file__).resolve().parents[2]
path_project = pathlib.Path('D:\Projects', 'adventOfCode2018')
os.chdir(path_project)

# Ingest the data
df = ingest_input(path_project.joinpath('Day1','input.csv'))

# Convert to a list for easier iteration
list_freq = list(df['change'])

#------------------------------------------------------------------------------
# Day 1, Part 1
#------------------------------------------------------------------------------

# Starting with a value of 0, iterate through every frequency change
value = 0
for freq in list_freq:
    # Increment the frequency
    value = increment_frequency(value, freq)
    
#------------------------------------------------------------------------------
# Day 1, Part 2
#------------------------------------------------------------------------------
# Starting with a value of 0, iterate through every frequency change
status = False    # status indicator for 2nd frequency achievement
value = 0         # starting value of frequency
list_index = 0    # index of position in frequency list
set_values = set()  # list for recording frequencies that have been "achieved"

# Iterate over the list of frequencies until status is True
while status != True:
    # Obtain the value in which to increment the frequency
    freq, list_index = advance_list(list_index)
    # Increment the frequency
    value = increment_frequency(value, freq)
    # Check if the frequency has already been achieved
    status, set_values = check_frequency_history(value, set_values)
    # Status report
    if list_index%100==0:
        print(list_index)