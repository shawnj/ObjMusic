from .tools import *
import sys

KEY = None
SCALE = None
PITCH_X = None
PITCH_Y = None
TIME_SET = None
TIME_X = None
TIME_Y = None
ORDER = None

def main():
   __p = objmusic.tools.PitchSet(SCALE,KEY,PITCH_X,PITCH_Y).get_grid()
   __t = objmusic.tools.TimeSet(TIME_SET,TIME_X,TIME_Y).get_grid()
   # __o = obj

if __name__ == '__main__':
    main()