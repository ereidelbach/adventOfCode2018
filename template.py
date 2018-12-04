#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:52:46 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day XX challenge 
        * https://adventofcode.com/2018/day/XX

    ****** PART 1 ******

    
    ****** PART 2 ******

"""
 
#==============================================================================
# Package Import
#==============================================================================
import numpy as np
import os
import pandas as pd
import pathlib

#==============================================================================
# Function Definitions / Reference Variable Declaration
#==============================================================================
def ingest_input(file_input):
    '''
    Purpose: Ingest data given a specific filename or filepath

    Input: 
        (1) file_input (string): Filename of data for part 1 challenge
    
    Output: 
        (1) NONE 
    '''
    with open(file_input, 'r') as f:
        content = f.readlines()
    
    return content

def function_name(var1, var2, var3):
    '''
    Purpose: Stuff goes here

    Input:   
        (1) var1 (type): description
        (2) var2 (type): description
        (3) var3 (type): description
    
    Output: 
        (1) output1 (type): description
    '''
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
path_project = pathlib.Path('/home/ejreidelbach/Projects/adventOfCode2018')
os.chdir(path_project)

# Ingest the data
list_claims = ingest_input(path_project.joinpath('Day4','input.txt'))