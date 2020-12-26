#! /usr/local/bin/python3 

import objmusic
import sys

KEY = sys.argv[1]
SCALE = sys.argv[2]
PITCH_X = sys.argv[3]
PITCH_Y = sys.argv[4]
TIMESET = sys.argv[5]
TIME_X = sys.argv[6]
TIME_Y = sys.argv[7]
NUMBER_OF_NOTES = sys.argv[8]
OUTPUT_FILE = sys.argv[9]

input_list = [
    KEY,
    SCALE,
    PITCH_X,
    PITCH_Y,    
    TIMESET,
    TIME_X,
    TIME_Y,
    NUMBER_OF_NOTES,
    OUTPUT_FILE,
]

# Returns midi file and prints output from selection

print(objmusic.main(input_list)) 