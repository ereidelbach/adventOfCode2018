#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:10:43 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day 14 challenge 
        * https://adventofcode.com/2018/day/14

    ****** PART 1 ******
    The Elves are trying to come up with the ultimate hot chocolate recipe; 
    they're even maintaining a scoreboard which tracks the quality score (0-9) 
    of each recipe.

    Only two recipes are on the board: the first recipe got a score of 3, the 
    second, 7. Each of the two Elves has a current recipe: the first Elf starts 
    with the first recipe, and the second Elf starts with the second recipe.

    To create new recipes, the two Elves combine their current recipes. This 
    creates new recipes from the digits of the sum of the current recipes' 
    scores. With the current recipes' scores of 3 and 7, their sum is 10, and 
    so two new recipes would be created: the first with score 1 and the second 
    with score 0. If the current recipes' scores were 2 and 3, the sum, 5, 
    would only create one recipe (with a score of 5) with its single digit.
    
    The new recipes are added to the end of the scoreboard in the order they 
    are created. So, after the first round, the scoreboard is 3, 7, 1, 0.
    
    After all new recipes are added to the scoreboard, each Elf picks a new 
    current recipe. To do this, the Elf steps forward through the scoreboard 
    a number of recipes equal to 1 plus the score of their current recipe. So, 
    after the first round, the first Elf moves forward 1 + 3 = 4 times, while 
    the second Elf moves forward 1 + 7 = 8 times. If they run out of recipes, 
    they loop back around to the beginning. After the first round, both Elves 
    happen to loop around until they land on the same recipe that they had in 
    the beginning; in general, they will move to different recipes.
    
    Drawing the first Elf as parentheses and the second Elf as square brackets, 
    they continue this process:
    
        (3)[7]
        (3)[7] 1  0 
         3  7  1 [0](1) 0 
         3  7  1  0 [1] 0 (1)
        (3) 7  1  0  1  0 [1] 2 
         3  7  1  0 (1) 0  1  2 [4]
         3  7  1 [0] 1  0 (1) 2  4  5 
         3  7  1  0 [1] 0  1  2 (4) 5  1 
         3 (7) 1  0  1  0 [1] 2  4  5  1  5 
         3  7  1  0  1  0  1  2 [4](5) 1  5  8 
         3 (7) 1  0  1  0  1  2  4  5  1  5  8 [9]
         3  7  1  0  1  0  1 [2] 4 (5) 1  5  8  9  1  6 
         3  7  1  0  1  0  1  2  4  5 [1] 5  8  9  1 (6) 7 
         3  7  1  0 (1) 0  1  2  4  5  1  5 [8] 9  1  6  7  7 
         3  7 [1] 0  1  0 (1) 2  4  5  1  5  8  9  1  6  7  7  9 
         3  7  1  0 [1] 0  1  2 (4) 5  1  5  8  9  1  6  7  7  9  2 
    
    The Elves think their skill will improve after making a few recipes (your 
    puzzle input). However, that could take ages; you can speed this up 
    considerably by identifying the scores of the ten recipes after that. 
    For example:
    
        - If the Elves think their skill will improve after making 9 recipes, 
            the scores of the ten recipes after the first nine on the 
            scoreboard would be 5158916779 (highlighted in the last line of 
            the diagram).
        - After 5 recipes, the scores of the next ten would be 0124515891.
        - After 18 recipes, the scores of the next ten would be 9251071085.
        - After 2018 recipes, the scores of the next ten would be 5941429882.
    
    What are the scores of the ten recipes immediately after the number of 
    recipes in your puzzle input?
    
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
day = '14'

# Your puzzle input is 260321.
input = 260321

#------------------------------------------------------------------------------
# Part 1.  What are the scores of the ten recipes immediately after the number 
#           of recipes in your puzzle input?
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Part 2.
#------------------------------------------------------------------------------