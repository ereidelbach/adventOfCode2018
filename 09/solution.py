#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:25:08 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day 9 challenge 
        * https://adventofcode.com/2018/day/9

    ****** PART 1 ******
    The Elves play this game by taking turns arranging the marbles in a circle 
    according to very particular rules. The marbles are numbered starting with 
    0 and increasing by 1 until every marble has a number.

    First, the marble numbered 0 is placed in the circle. At this point, while 
    it contains only a single marble, it is still a circle: the marble is both 
    clockwise from itself and counter-clockwise from itself. This marble is 
    designated the current marble.

    Then, each Elf takes a turn placing the lowest-numbered remaining marble 
    into the circle between the marbles that are 1 and 2 marbles clockwise of 
    the current marble. (When the circle is large enough, this means that there 
    is one marble between the marble that was just placed and the current 
    marble.) The marble that was just placed then becomes the current marble.

    However, if the marble that is about to be placed has a number which is a 
    multiple of 23, something entirely different happens. First, the current 
    player keeps the marble they would have placed, adding it to their score. 
    In addition, the marble 7 marbles counter-clockwise from the current marble 
    is removed from the circle and also added to the current player's score. 
    The marble located immediately clockwise of the marble that was removed 
    becomes the new current marble.

    For example, suppose there are 9 players. After the marble with value 0 is 
    placed in the middle, each player (shown in square brackets) takes a turn. 
    The result of each of those turns would produce circles of marbles like 
    this, where clockwise is to the right and the resulting current marble is 
    in parentheses:

    [-] (0)
    [1]  0 (1)
    [2]  0 (2) 1 
    [3]  0  2  1 (3)
    [4]  0 (4) 2  1  3 
    [5]  0  4  2 (5) 1  3 
    [6]  0  4  2  5  1 (6) 3 
    [7]  0  4  2  5  1  6  3 (7)
    [8]  0 (8) 4  2  5  1  6  3  7 
    [9]  0  8  4 (9) 2  5  1  6  3  7 
    [1]  0  8  4  9  2(10) 5  1  6  3  7 
    [2]  0  8  4  9  2 10  5(11) 1  6  3  7 
    [3]  0  8  4  9  2 10  5 11  1(12) 6  3  7 
    [4]  0  8  4  9  2 10  5 11  1 12  6(13) 3  7 
    [5]  0  8  4  9  2 10  5 11  1 12  6 13  3(14) 7 
    [6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7(15)
    [7]  0(16) 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15 
    [8]  0 16  8(17) 4  9  2 10  5 11  1 12  6 13  3 14  7 15 
    [9]  0 16  8 17  4(18) 9  2 10  5 11  1 12  6 13  3 14  7 15 
    [1]  0 16  8 17  4 18  9(19) 2 10  5 11  1 12  6 13  3 14  7 15 
    [2]  0 16  8 17  4 18  9 19  2(20)10  5 11  1 12  6 13  3 14  7 15 
    [3]  0 16  8 17  4 18  9 19  2 20 10(21) 5 11  1 12  6 13  3 14  7 15 
    [4]  0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15 
    [5]  0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 
    [6]  0 16  8 17  4 18 19  2(24)20 10 21  5 22 11  1 12  6 13  3 14  7 15 
    [7]  0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15

    The goal is to be the player with the highest score after the last marble 
    is used up. Assuming the example above ends after the marble numbered 25, 
    the winning score is 23+9=32 (because player 5 kept marble 23 and removed 
    marble 9, while no other player got any points in this very short example 
    game).
    
    Here are a few more examples:

        10 players; last marble is worth 1618 points: high score is 8317
        13 players; last marble is worth 7999 points: high score is 146373
        17 players; last marble is worth 1104 points: high score is 2764
        21 players; last marble is worth 6111 points: high score is 54718
        30 players; last marble is worth 5807 points: high score is 37305

    What is the winning Elf's score?
    
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
day = '9'

# Download and ingest the data for today's challenge
data_raw = ingestInput(path_project.joinpath(day.zfill(2), 'input.txt'))[0]

#------------------------------------------------------------------------------
# Part 1.  What is the winning Elf's score?
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Part 2.
#------------------------------------------------------------------------------