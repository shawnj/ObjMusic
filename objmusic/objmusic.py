from .tools import *
import sys

KEY = "C"
SCALE = "Major"
PITCH_X = 4
PITCH_Y = 5
TIME_SET = [2,4,4,8,16,16,8]
TIME_X = 3
TIME_Y = 4
NUM_NOTES = 10

def main():
    __p = PitchSet(SCALE,KEY,PITCH_X,PITCH_Y).get_grid()
    __t = TimeSet(TIME_SET,TIME_X,TIME_Y).get_grid()
    __o = OrderSet(NUM_NOTES).get_order()
    __v = Variation(__o,__p,__t)

    return __v.return_variation()

if __name__ == '__main__':
    main()