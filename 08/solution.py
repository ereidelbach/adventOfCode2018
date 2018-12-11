#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 08:36:45 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day 8 challenge 
        * https://adventofcode.com/2018/day/8

    ****** PART 1 ******
    The navigation system's license file consists of a list of numbers (your 
    puzzle input). The numbers define a data structure which, when processed, 
    produces some kind of tree that can be used to calculate the license number.

    The tree is made up of nodes; a single, outermost node forms the tree's 
    root, and it contains all other nodes in the tree (or contains nodes that 
    contain nodes, and so on).

    Specifically, a node consists of:
        - A header, which is always exactly two numbers:
            * The quantity of child nodes.
            * The quantity of metadata entries.
        - Zero or more child nodes (as specified in the header).
        - One or more metadata entries (as specified in the header).

    Each child node is itself a node that has its own header, child nodes, and 
    metadata. For example:

    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    A----------------------------------
        B----------- C-----------
                         D-----

    In this example, each node of the tree is also marked with an underline 
    starting with a letter for easier identification. In it, there are four 
    nodes:
        - A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
        - B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
        - C, which has 1 child node (D) and 1 metadata entry (2).
        - D, which has 0 child nodes and 1 metadata entry (99).

    The first check done on the license file is to simply add up all of the 
    metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

    What is the sum of all metadata entries?
    
    ****** PART 2 ******

"""
 
#==============================================================================
# Package Import
#==============================================================================
import os
import pandas as pd
import pathlib

#==============================================================================
# Function Definitions / Reference Variable Declaration
#==============================================================================
def ingestInput(file_input):
    '''
    Purpose: Ingest data given a specific filename or filepath

    Input: 
        (1) file_input (string): Filename of data for part 1 challenge
    
    Output: 
        (1) The data for the day's challenge (input.txt) in the folder /XX/ 
                where XX represents the day of the challenge (e.g. 05, 23)
    '''
    with open(file_input, 'r') as f:
        content = f.readlines()
        
    # Strip trailing new line from strings in the list
    for item in content:
        content[content.index(item)] = item.strip()
    
    return content

def functionName(var1, var2, var3):
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

# Set the day of the project
day = '8'

# Download and ingest the data for today's challenge
data_raw = ingestInput(path_project.joinpath(day.zfill(2), 'input.txt'))
data_raw = data_raw[0]

#------------------------------------------------------------------------------
# Part 1.  What is the sum of all metadata entries?
#------------------------------------------------------------------------------
def readNode(list_metadata, list_data):   
    # Extract the # of children and the # of metadata elements
    num_child_nodes, num_metadata_entries = list_data[:2]
    list_data = list_data[2:]
    
    for num in range(num_child_nodes):
        readNode(list_metadata, list_data)
    
    # Base case
    # No children exist -- return the metadata values
    if num_child_nodes == 0:
        print('In base: # meta_data entries is: ' + str(num_metadata_entries))
        for entry in range(2,num_metadata_entries+2):
            print('Metadata: ' + str(list_data[entry]))
            list_metadata.append(int(list_data[entry]))
        return list_metadata
    # Recurseive case
    # Thread the state through the recursive call
    else:
        return readNode(list_metadata, list_data[2:])

test = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
test = test.split(' ')
test = [int(x) for x in test]
print(readNode([], test))
#------------------------------------------------------------------------------
# Part 2.
#------------------------------------------------------------------------------