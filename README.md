# ObjMusic

## Description

Output of objmusic library will be a piece of melodic content based upon the inputs given.

Three parts are used to devise the output as needed.

1.  PitchSet
2.  TimeSet
3.  DesignSet

The sets will be combined to complete a single musical form.
## Usage

```
import objmusic

KEY = "C"
SCALE = "Major"
OUTPUT_FILE = "path.mid"
PITCH_X = 4
PITCH_Y = 5
TIMESET = "One"
TIME_X = 3
TIME_Y = 4
NUMBER_OF_NOTES = 10
OCTAVE = 4

# Returns midi file and prints output from selection

objmusic.main([SCALE,PITCH_X,PITCH_Y,TIMESET,TIME_X,TIME_Y,NUMBER_OF_NOTES,OUTPUT_FILE,OCTAVE,KEY]) 
```
