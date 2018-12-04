#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 06:52:46 2018

@author: ejreidelbach

:DESCRIPTION:
    - Day 4 challenge 
        * https://adventofcode.com/2018/day/4

    ****** PART 1 ******
    Timestamps are written using year-month-day hour:minute format. The guard 
    falling asleep or waking up is always the one whose shift most recently 
    started. Because all asleep/awake times are during the midnight hour 
    (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those 
    events.
 
    The columns are Date, which shows the month-day portion of the relevant 
    day; ID, which shows the guard on duty that day; and Minute, which shows 
    the minutes during which the guard was asleep within the midnight hour. 
    (The Minute column's header shows the minute's ten's digit in the first 
    row and the one's digit in the second row.) Awake is shown as ., and asleep 
    is shown as #.

    Note that guards count as asleep on the minute they fall asleep, and they 
    count as awake on the minute they wake up. For example, because Guard #10 
    wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

    If you can figure out the guard most likely to be asleep at a specific 
    time, you might be able to trick that guard into working tonight so you can 
    have the best chance of sneaking in. You have two strategies for choosing 
    the best guard/minute combination.

    Strategy 1: Find the guard that has the most minutes asleep. What minute 
    does that guard spend asleep the most?       
    
    In the example above, Guard #10 spent the most minutes asleep, a total of 
    50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes 
    (10+10+10). Guard #10 was asleep most during minute 24 (on two days, 
    whereas any other minute the guard was asleep was only seen on one day).

    While this example listed the entries in chronological order, your entries 
    are in the order you found them. You'll need to organize them before they 
    can be analyzed.

    What is the ID of the guard you chose multiplied by the minute you chose? 
    (In the above example, the answer would be 10 * 24 = 240.)    
        
    ****** PART 2 ******
    Strategy 2: Of all guards, which guard is most frequently asleep on the 
    same minute?

    In the example above, Guard #99 spent minute 45 asleep more than any other 
    guard or minute - three times in total. (In all other cases, any guard 
    spent any minute asleep at most twice.)

    What is the ID of the guard you chose multiplied by the minute you chose? 
    (In the above example, the answer would be 99 * 45 = 4455.)
"""
 
#==============================================================================
# Package Import
#==============================================================================
import datetime # for timestamp management
import numpy as np
import os
import pandas as pd
import pathlib
import tqdm

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
        
    # Strip trailing new line from strings in the list
    for item in content:
        content[content.index(item)] = item.strip()
    
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
data_raw = ingest_input(path_project.joinpath('Day4','input.txt'))

#------------------------------------------------------------------------------
# Part 1:  Find the guard that has the most minutes asleep.  
#           - What minute does that guard spend asleep the most?
#           - What is the ID of that guard multipled by the minute chosen?
#------------------------------------------------------------------------------

### Step 1:  Sort the data into chronological order
data_clean = []
for data in data_raw:
    time_str = data.split(']')[0].split('[')[1]
    time_stamp = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M')
    event = data.split('] ')[1]
    data_clean.append([time_stamp, event])

# convert the data to a DataFrame    
df = pd.DataFrame(data_clean, columns = ['timestamp', 'event'])

# sort the DataFrame by timestamp and reset the index
df = df.sort_values('timestamp')
df = df.reset_index(drop=True)

### Step 2:  Create a column that indicates the guard it's associated with
###             and whether or not the guard is awake or asleep
list_events = list(df['event'])
list_guards = []
guard = ''

for event in list_events:
    # Guard status
    if 'Guard' in event:
        guard = event.split('Guard #')[1].split(' ')[0]
    list_guards.append(guard)

    
df['guard'] = list_guards

### Step 3:  Create a column that calculates how many minutes the guard slept
list_time = df['timestamp']
list_time_asleep = []
time_begin_sleep = ''
for time, event in zip(list_time, list_events):
    if 'asleep' in event:
        time_begin_sleep = time
        list_time_asleep.append(0)
    elif 'wakes' in event:
        list_time_asleep.append((time - time_begin_sleep).total_seconds())
        time_begin_sleep = ''
    # covers guard changes
    else:
        list_time_asleep.append(0)
        
df['time_asleep'] = list_time_asleep

### Step 4:  Find the guard with the most minutes asleep
sleepiest_id = df.groupby(['guard'])['time_asleep'].sum().sort_values(
        ascending = False).index[0]

### Step 5:  Find the minute the guard slept the most
df_sleepy = df[df['guard'] == sleepiest_id]

dict_guard = {}
for a in range(0,60):
    dict_guard[a] = 0
start_min = ''
start_time = ''

for row_idx, row in df_sleepy.iterrows():
    if 'asleep' in row['event']:
        start_min = row['timestamp'].minute
        start_time = row['timestamp']
    elif 'wakes' in row['event']:
        stop_time = row['timestamp']
        time_diff = int((stop_time-start_time).total_seconds()/60)
        minute = 0
        while minute < time_diff:
            sleep_min = (start_min + minute)%60
            dict_guard[sleep_min] += 1
            minute += 1
                
df_minutes = pd.DataFrame.from_dict(dict_guard, orient='index', columns=['count'])
sleepy_minute = df_minutes['count'].sort_values(ascending=False).index[0]
                
### Step 6:  What is the ID of the guard multiple by the minute chosen?
print('ID multipled by minute: ' + str(int(sleepiest_id) * sleepy_minute))

#------------------------------------------------------------------------------
# Part 2:  Find the guard that is most frequenly asleep on the same minute 
#           - What is the ID of the guard you chose multipled by the minute
#               they are most commonly asleep
#------------------------------------------------------------------------------
# create a dict for storing sleep-by-minute counts for all guards
dict_guards = {}

# create a unique list of all guard IDs
set_ids = set(list_guards)

# iterate over all guards
for guard_id in tqdm.tqdm(set_ids):
    
    dict_guard = {}
    for a in range(0,60):
        dict_guard[a] = 0
    start_min = ''
    start_time = ''
    
    # compute the sleep-by-minute count for the guard
    df_guard = df[df['guard'] == guard_id]
    for row_idx, row in df_guard.iterrows():
        
        if 'asleep' in row['event']:
            start_min = row['timestamp'].minute
            start_time = row['timestamp']
        elif 'wakes' in row['event']:
            stop_time = row['timestamp']
            time_diff = int((stop_time-start_time).total_seconds()/60)
            minute = 0
            while minute < time_diff:
                sleep_min = (start_min + minute)%60
                dict_guard[sleep_min] += 1
                minute += 1
                
    df_minutes = pd.DataFrame.from_dict(dict_guard, orient='index', columns=['count'])
    sleepy_amount = df_minutes['count'].sort_values(ascending=False).iloc[0]
    sleepy_minute = df_minutes['count'].sort_values(ascending=False).index[0]
    
    dict_guards[guard_id] = {
            'minute' : sleepy_minute,
            'number of times slept' : sleepy_amount,
            }

# sort the dictionary of guards by the guard who slept the most @ the same min.
sleepiest_guard = ''
sleepiest_time = 0
for key, value in dict_guards.items():
    if dict_guards[key]['number of times slept'] > sleepiest_time:
        sleepiest_time = dict_guards[key]['number of times slept']
        sleepiest_guard = key

# Output the results
print('The sleepiest guard was #: ' + str(sleepiest_guard))
print('They were asleep on minute ' 
      + str(dict_guards[sleepiest_guard]['minute']) + ', ' + str(sleepiest_time)
      + ' times!')
print('The final answer (guard ID multiplied by the minute chosen) is: ' +
      str(int(sleepiest_guard)*dict_guards[sleepiest_guard]['minute']))