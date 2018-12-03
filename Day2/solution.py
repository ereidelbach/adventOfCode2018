#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:33:02 2018

@author: Eric Reidelbach

:DESCRIPTION:
    - Day 2 challenge 
        * https://adventofcode.com/2018/day/2

    ****** PART 1 ******
    To make sure you didn't miss any, you scan the likely candidate boxes 
    again, counting the number that have an ID containing exactly two of 
    any letter and then separately counting those with exactly three of any 
    letter. You can multiply those two counts together to get a rudimentary 
    checksum and compare it to what your device predicts.

    For example, if you see the following box IDs:

        abcdef contains no letters that appear exactly two or three times.
        bababc contains two a and three b, so it counts for both.
        abbcde contains two b, but no letter appears exactly three times.
        abcccd contains three c, but no letter appears exactly two times.
        aabcdd contains two a and two d, but it only counts once.
        abcdee contains two e.
        ababab contains three a and three b, but it only counts once.

    Of these box IDs, four of them contain a letter which appears exactly 
    twice, and three of them contain a letter which appears exactly three 
    times. Multiplying these together produces a checksum of 4 * 3 = 12.

    What is the checksum for your list of box IDs?
    
    ****** PART 2 ******
    Confident that your list of box IDs is complete, you're ready to find the 
    boxes full of prototype fabric.

    The boxes will have IDs which differ by exactly one character at the same 
    position in both strings. For example, given the following box IDs:
    
    What letters are common between the two correct box IDs? (In the example 
    above, this is found by removing the differing character from either ID, 
    producing fgij.)
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

def countLetters(boxID):
    '''
    Purpose: Check if a string contains exactly two or three of any letter

    Input: 
        (1) boxID (string):  ID of a box being scanned (format ~= 'abcabc')
    
    Output: 
        (1) matchTwo (boolean): True if string contains exactly two of any 
                letter, False if it does not
        (2) matchThree (boolean): True if string contains exactly three of any
                letter, False if it does not
    '''
    # Create a dictionary containing the letters in a string and the numer
    #   of times it has been seen
    count_dict = {}
    for letter in boxID:
        # if the letter exists in the dictionary, retrieve the old count and +1
        if letter in list(count_dict):
           count = count_dict[letter]
           count_dict[letter] = count + 1
        # if the letter does not exist, add it to the dict and set count = 1
        else:
            count_dict[letter] = 1
    
    # if a count of 2 exists in the dictionary, return true for matchTwo, 
    #   otherwise return false  -- the same applies to matchThree except
    #   we're tracking a count of 3 
    if 2 in count_dict.values():
        matchTwo = True
    else:
        matchTwo = False
    if 3 in count_dict.values():
        matchThree = True
    else:
        matchThree = False
        
    return matchTwo, matchThree    

def checkSum(count_two, count_three):
    '''
    Purpose: Determine the checksum for the given input by multiplying the 
        count of boxIDs containing exactly two letters by the count of boxIDs
        containing exactly three letters
    
    Input:
        (1) count_two (float): count of boxIDs containing exactly two letters
        (2) count_three (float): count of boxIDs containing exactly three letters
        
    Output:
        (1) checksum (float): calculated checksum found by multiplying 
                count_two by count_three
    '''    
    checksum = count_two * count_three
    return checksum

        

def checkLetterDifferences (boxID, list_boxIDs):
    '''
    Purpose: Check if IDs differ by exactly one character at the same position
        in both strings.  For example, 'fghij' and 'fguij' differ by exactly
        one character, the third ('h' and 'u').
    
    Input:
        (1) boxID (string): first boxID to be compared to all other IDs
        (2) list_boxIDs (list): list of boxIDs to compare the boxID to
        
    Output:
        (1) found_match (boolean): True if the number of letters different in 
                the string is equal to 1, otherwise False
        (2) found_match_word (string): Box ID that differs by only one letter
    '''   
    # Iterate over every letter in the box IDs and compare the strings to see
    #   if they match; if they don't match, increment the 'miss' counter by 1.
    #   If the 'miss' counter exceeds 1, sto the search as these are not the
    #   right boxes.
    for compID in list_boxIDs:
        count_miss = 0
        for x, y in zip(boxID, compID):
            if x != y:
                count_miss += 1
            if count_miss == 2:
                break
        if count_miss == 1:
            return True, compID
    return False, ''
    
def compareStrings(A, B):
    '''
    Purpose: Determine the shared letters betwen two strings
    
    Input:
        (1) A (string): first boxID to be compared
        (2) B (string): second boxID to be compared
        
    Output:
        (1) matching_letters (list): Letters that exist in both strings
    '''   
    matching_letters = []
    for x, y in zip(A, B):
        if x == y:
            matching_letters.append(x)

    return matching_letters            
    
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
#path_project = pathlib.Path(__file__).resolve().parents[2]
path_project = pathlib.Path('D:\Projects', 'adventOfCode2018')
os.chdir(path_project)

# Ingest the data
df = ingest_input(path_project.joinpath('Day2','input.csv'))

# Create a list out of the box IDs
list_boxIDs = list(df['ID'])

#------------------------------------------------------------------------------
# Day 2, Part 1
#------------------------------------------------------------------------------
# Calculate the count for box IDs containing exactly two or three letters
list_twos = []
list_threes = []
for boxID in list_boxIDs:
    two, three = countLetters(boxID)
    list_twos.append(two)
    list_threes.append(three)
    
count_two = sum(list_twos)
count_three = sum(list_threes)
        
# Calculate the checksum
answer = checkSum(count_two, count_three)
print('The Checksum is: ' + str(answer))

#------------------------------------------------------------------------------
# Day 2, Part 2
#------------------------------------------------------------------------------
# Iterate over every string in the list and compare it to all other strings
for boxID in list_boxIDs:
    # Test for differences between letters within an ID and all other IDs
    test_miss, matchingID = checkLetterDifferences(boxID, list_boxIDs)

    # If a difference between strings of just one letter is found, find the 
    #   common letters between the two box IDs
    if test_miss == True:
        print(''.join(compareStrings(boxID, matchingID)))
