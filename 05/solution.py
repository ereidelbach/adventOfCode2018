#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 07:05:07 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day 5 challenge 
        * https://adventofcode.com/2018/day/5

    ****** PART 1 ******
    The polymer is formed by smaller units which, when triggered, react with 
    each other such that two adjacent units of the same type and opposite 
    polarity are destroyed. Units' types are represented by letters; units' 
    polarity is represented by capitalization. For instance, r and R are units 
    with the same type but opposite polarity, whereas r and s are entirely 
    different types and do not react.

    For example:

        In aA, a and A react, leaving nothing behind.
        In abBA, bB destroys itself, leaving aA. As above, this then destroys 
            itself, leaving nothing.
        In abAB, no two adjacent units are of the same type, and so nothing happens.
        In aabAAB, even though aa and AA are of the same type, their polarities 
            match, and so nothing happens.

    Now, consider a larger example, dabAcCaCBAcCcaDA:

        dabAcCaCBAcCcaDA  The first 'cC' is removed.
        dabAaCBAcCcaDA    This creates 'Aa', which is removed.
        dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
        dabCBAcaDA        No further actions can be taken.

    After all possible reactions, the resulting polymer contains 10 units.    

    How many units remain after fully reacting the polymer you scanned? 
    
    ****** PART 2 ******

    Time to improve the polymer.

    One of the unit types is causing problems; it's preventing the polymer from 
    collapsing as much as it should. Your goal is to figure out which unit type 
    is causing the most problems, remove all instances of it (regardless of 
    polarity), fully react the remaining polymer, and measure its length.

    For example, again using the polymer dabAcCaCBAcCcaDA from above:

        Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer 
            produces dbCBcD, which has length 6.
        Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this 
            polymer produces daCAcaDA, which has length 8.
        Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer 
            produces daDA, which has length 4.
        Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this 
            polymer produces abCBAc, which has length 6.

    In this example, removing all C/c units was best, producing the answer 4.

    What is the length of the shortest polymer you can produce by removing all 
    units of exactly one type and fully reacting the result?
"""
 
#==============================================================================
# Package Import
#==============================================================================
import os
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

def removeReactions(polymer):
    '''
    Purpose: Iterate through a polymer (i.e. a string) repeatedly until all
        possible reactions have been removed.

    Input:   
        (1) polymer (string): a string composed of upper-case and lower-case
                letters simulating a polymer. 
    
    Output: 
        (1) length_polymer (int): Remaining length of the polymer (i.e. string)
    '''
    scan_complete = False   # False implies reactions were in the previous
                            #   pass of the polymer and more scanning is needed    
    while scan_complete == False:
        polymer, scan_complete = triggerReactions(polymer)
    
    print('The length of the polymer after reactions is {len} units'.format(
            len = len(polymer)))
    return len(polymer)
    
def triggerReactions(polymer):
    '''
    Purpose: Iterate through a polymer (i.e a string) and identify any 
        occurrences of a lower case letter being followed by the capitalized
        version of the same letter. If this occurs, remove both letters. Do
        this for every letter in the alphabet.

    Input:   
        (1) polymer (string): a string composed of upper-case and lower-case
                letters simulating a polymer.     
    Output: 
        (1) polymer (string): the updated polymer in which
                reactions have been found and removed over the course of a 
                single pass through the alphabet
        (2) scan_complete (boolean): a status indicator which tells us whether
                or not a reaction was removed from the polymer (True = yes)
    '''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    scan_complete = True   # assume we won't see any reactions
    
    for letter in alphabet:
        aA = letter.lower() + letter
        Aa = letter + letter.lower()
        if (aA in polymer) or (Aa in polymer):
            scan_complete = False  # if we do see a reaction, set to False
        polymer = polymer.replace(aA, '').replace(Aa,'')

    return polymer, scan_complete

def improvePolymer(polymer):
    '''
    Purpose: Attempt to improve the polymer by determining which unit type 
        (i.e. letter) is causing the most problems by removing all instances of 
        it (regardless of polarity). Then fully react the reamining polymer and 
        measure its length.
        
    Input:   
        (1) polymer (string): a string composed of upper-case and lower-case
                letters simulating a polymer. 
        
    Output:
        (1) NONE
    '''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length_shortest = len(polymer)
    letter_shortest = ''
    
    for letter in alphabet:
        # remove the upper- and lower-case versions of the letter
        polymer_letter_removed = polymer.replace(
                letter.lower(),'').replace(letter,'')
        # test the length of the polymer after removing all reactions
        # if the resulting polymer is the shorest one yet, save it's length
        length_polymer = removeReactions(polymer_letter_removed)
        if length_polymer < length_shortest:
            length_shortest = length_polymer
            letter_shortest = letter
    print('The shortest list was {length}, as caused by letter {letter}'
          .format(length=length_shortest, letter=letter_shortest))
        
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
path_project = pathlib.Path('/home/ejreidelbach/Projects/adventOfCode2018')
os.chdir(path_project)

# Set the day of the project
day = '5'

# Download and ingest the data for today's challenge
data_raw = ingestInput(path_project.joinpath(day.zfill(2), 'input.txt'))

# Today's file is a long string, so let's remove the list element
data_raw = data_raw[0]

#------------------------------------------------------------------------------
# Part 1:  How many units remain after fully reacting the polymer you scanned?
#           - i.e. how many letters are left in the string?
#------------------------------------------------------------------------------
len_polymer = removeReactions(data_raw)

#------------------------------------------------------------------------------
# Part 2:  Determine which unit type (i.e. letter) is causing the most 
#           problems by removing all instances of it (regardless of polarity).
#           Then fully react the reamining polymer and measure its length.
#------------------------------------------------------------------------------
improvePolymer(data_raw)