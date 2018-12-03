#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 3 06:38:02 2018

@author: Eric Reidelbach

:DESCRIPTION:
    - Day 3 challenge 
        * https://adventofcode.com/2018/day/3

    ****** PART 1 ******
    The whole piece of fabric they're working on is a very large square - 
    at least 1000 inches on each side.

    Each Elf has made a claim about which area of fabric would be ideal for 
    Santa's suit. All claims have an ID and consist of a single rectangle 
    with edges parallel to the edges of the fabric. Each claim's rectangle 
    is defined as follows:

        * The number of inches between the left edge of the fabric and the left 
            edge of the rectangle.
        * The number of inches between the top edge of the fabric and the top 
            edge of the rectangle.
        * The width of the rectangle in inches.
        * The height of the rectangle in inches.

    A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 
    3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 
    4 inches tall. Visually, it claims the square inches of fabric represented 
    by # (and ignores the square inches of fabric represented by .) in the 
    diagram below:
    
    ****** PART 2 ******
    Amidst the chaos, you notice that exactly one claim doesn't overlap by 
    even a single square inch of fabric with any other claim. If you can 
    somehow draw attention to it, maybe the Elves will be able to make Santa's 
    suit after all!

    For example, in the claims above, only claim 3 is intact after all 
    claims are made.

    What is the ID of the only claim that doesn't overlap?
"""
 
#==============================================================================
# Package Import
#==============================================================================
import numpy as np
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
    with open(file_input, 'r') as f:
        content = f.readlines()
    
    return content

def make_fabric_grid():
    '''
    Purpose: Create a fabric grid that is slightly bigger than the estimated
        gride size of 1000 x 1000 (default to 1200 x 1200) just to on the safe
        side.  This grid represents the fabric structure used in this problem.

    Input: 
        (1) NONE
    
    Output: 
        (1) fabric_matrix (numpy matrix [i.e. 2-D array] of size 1200 x 1200)
                - default value for each cell is 0
    '''
    # default to 1200 x 1200 gride
    fabric_matrix = np.zeros((1200,1200))
    return fabric_matrix

def make_claims(claim):
    '''
    Purpose: For a given claim, identify the claim's X/Y coordinates and for
        every cell which the claim is 'claiming', increment the associated cell 
        count by 1.  For example, an X/Y coordinate having a value of 4 would 
        mean that 4 claims have been made for that cell.

    Input: 
        (1) claim (string): Fabric claim containing the claim's ID #, the 
                starting X/Y coordinates and the number of inches wide and high
                that the claim is being made for
                (e.g. #1295 @ 312,342: 21x17 ---- Claim number 1295 starting at
                 312 inches in from the lef (x) and 342 inches from the top (Y)
                 21 inches in width (x) and 17 inches in height(y))
    
    Output: 
        (1) fabric_matrix (numpy matrix [i.e. 2-D array] of size 1200 x 1200)
                - cell values have been updated to reflect the correct # of
                    claims for each cell
    '''
    # obtain basic information about the claim from the string
    claim_start_x = int(claim.split('@ ')[1].split(',')[0])
    claim_start_y = int(claim.split('@ ')[1].split(',')[1].split(':')[0])
    claim_len_x = int(claim.split('x')[0].split(': ')[1])
    claim_len_y = int(claim.split('x')[1].strip())
    
    # introduce offset to account for real counting vs python counting
    claim_start_x = claim_start_x + 1
    claim_start_y = claim_start_y + 1
    
    # make claim by starting at the starting point and incrementing the claim
    #   count for a given cell by 1
    # for every row
    y = claim_start_y
    while y < (claim_start_y + claim_len_y):
        # for every column
        x = claim_start_x
        while x < (claim_start_x + claim_len_x):
            # increment the [x][y] coordinate's 'claim count'
            try:
                fabric_matrix[x][y] += 1
            except:
                print('x is: ' + str(x) + ', y is: ' + str(y))
                print('current value is: ' + str(fabric_matrix[x][y]))
            x += 1  # move to the next cell in the row
        y += 1      # move up a row in the column
    return fabric_matrix    

def make_claims_with_ids(claim):
    '''
    Purpose: For a given claim, identify the claim's X/Y coordinates and for
        every cell which the claim is 'claiming', set the value of the cell
        to equal the claim's ID.  If a claim already exists for that cell,
        set the cell's value to 99 so that we know multiple claims are being
        made.  

    Input: 
        (1) claim (string): Fabric claim containing the claim's ID #, the 
                starting X/Y coordinates and the number of inches wide and high
                that the claim is being made for
                (e.g. #1295 @ 312,342: 21x17 ---- Claim number 1295 starting at
                 312 inches in from the lef (x) and 342 inches from the top (Y)
                 21 inches in width (x) and 17 inches in height(y))
    
    Output: 
        (1) fabric_matrix (numpy matrix [i.e. 2-D array] of size 1200 x 1200)
                - cell values have been updated to reflect the ID's of the
                    claims "claiming" each cell -- value == 99 if multiple
                    claims exist
    '''
    # obtain basic information about the claim from the string
    claim_id = int(claim.split(' @')[0].split('#')[1])
    claim_start_x = int(claim.split('@ ')[1].split(',')[0])
    claim_start_y = int(claim.split('@ ')[1].split(',')[1].split(':')[0])
    claim_len_x = int(claim.split('x')[0].split(': ')[1])
    claim_len_y = int(claim.split('x')[1].strip())
    
    # introduce offset to account for real counting vs python counting
    claim_start_x = claim_start_x + 1
    claim_start_y = claim_start_y + 1
    
    # make claim by starting at the starting point and inserting the ID of the
    #   claim into an associated cell -- if a claim has already been made 
    #   (i.e. the cell value does not equal 0) set the value to 99 so that it
    #    is known the cell has already been claimed
    # for every row
    y = claim_start_y
    while y < (claim_start_y + claim_len_y):
        # for every column
        x = claim_start_x
        while x < (claim_start_x + claim_len_x):
            # if the cell has already been claimed, set the value to 99
            if fabric_matrix[x][y] != 0:
                fabric_matrix[x][y] = 99
            # if the cell has not been claimed, set the value to the claim ID
            else:
                fabric_matrix[x][y] = claim_id
            x += 1  # move to the next cell in the row
        y += 1      # move up a row in the column     
    return fabric_matrix    

def validate_claims(claim, matrix):
    '''
    Purpose: For a given claim, identify the claim's X/Y coordinates and for
        every cell which the claim is 'claiming', determine if the cell has 
        been claimed by another cell (i.e. the cell's value equals 1 and not 
        99).  If the process of iterating through every cell is completed and
        a 99 has not been found, all the claim's 'claims' are valid and the
        claim ID number will be output to the screen.

    Input: 
        (1) claim (string): Fabric claim containing the claim's ID #, the 
                starting X/Y coordinates and the number of inches wide and high
                that the claim is being made for
                (e.g. #1295 @ 312,342: 21x17 ---- Claim number 1295 starting at
                 312 inches in from the lef (x) and 342 inches from the top (Y)
                 21 inches in width (x) and 17 inches in height(y))
        (2) matrix (numpy matrix [i.e. 2-D array] of size 1200 x 1200)
                - cell values contain the ID's of the claims 'claiming' each
                    cell --> a value of 99 means that cell has been 'claimed'
                    by multiple claims
    
    Output: 
        (1) NONE
    '''

    # obtain basic information about the claim from the string
    claim_id = int(claim.split(' @')[0].split('#')[1])
    claim_start_x = int(claim.split('@ ')[1].split(',')[0])
    claim_start_y = int(claim.split('@ ')[1].split(',')[1].split(':')[0])
    claim_len_x = int(claim.split('x')[0].split(': ')[1])
    claim_len_y = int(claim.split('x')[1].strip())
    
    # introduce offset to account for real counting vs python counting
    claim_start_x = claim_start_x + 1
    claim_start_y = claim_start_y + 1    
            
    # iterate through every cell a claim is making and determine if the claim
    #   has been made by multiple cell (i.e. cell == 99)
    y = claim_start_y
    while y < (claim_start_y + claim_len_y):
        # for every column
        x = claim_start_x
        while x < (claim_start_x + claim_len_x):
            # insert into correct [x][y] coordinate
            if fabric_matrix[x][y] == 99:
                return
            x += 1  # move to the next cell in the row
        y += 1      # move up a row in the column     
    
    print('Valid claim found: ' + str(claim_id))
    return
    
#==============================================================================
# Working Code
#==============================================================================

# Set the project working directory
#path_project = pathlib.Path(__file__).resolve().parents[2]
path_project = pathlib.Path('/home/ejreidelbach/Projects/adventOfCode2018')
os.chdir(path_project)

# Ingest the data
list_claims = ingest_input(path_project.joinpath('Day3','input.txt'))

#------------------------------------------------------------------------------
# Day 3, Part 1
#------------------------------------------------------------------------------
# How many square inches of fabric are within two or more claims?

# Initialize a fabric matrix
fabric_matrix = make_fabric_grid()

# for every claim, cycle over it and start adding claims to the grid
for claim in list_claims:
    fabric_matrix = make_claims(claim)

# We're interested in determining the number of cells with multiple claims
# Begin by subtracting out any cells claimed by only one claim 
#   --> set value = 0  
fabric_matrix[fabric_matrix == 1] = 0
# Set all cells claimed by mupltiple claims to 1
fabric_matrix[fabric_matrix >= 2] = 1

# Add together the value of all cells (i.e. all 1's) to determine the total 
#   inches of fabric claimed by multiple claims
np.sum(fabric_matrix)

#------------------------------------------------------------------------------
# Day 3, Part 2
#------------------------------------------------------------------------------

# Re-Initialize a fabric matrix
fabric_matrix = make_fabric_grid()

# for every claim, cycle over it and start adding claims to the grid
for claim in list_claims:
    fabric_matrix = make_claims_with_ids(claim)

# for every claim, cycle over it and determine if its claims are claimed by
#   any other claim
for claim in list_claims:
    validate_claims(claim, fabric_matrix)