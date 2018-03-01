from .tools import *
import sys
import random

def main(args):

    KEY = random.sample(["C","D","E","F","G","A"],1)[0]
    SCALE = args[0]
    PITCH_X = args[1]
    PITCH_Y = args[2]
    TIME_SET = args[3]
    TIME_X = args[4]
    TIME_Y = args[5]
    NUM_NOTES = args[6]
    
    __p = PitchSet(SCALE,KEY,PITCH_X,PITCH_Y).get_grid()
    __t = TimeSet(TIME_SET,TIME_X,TIME_Y).get_grid()
    __o = OrderSet(NUM_NOTES).get_order()
    __v = Variation(__o,__p,__t)

    return __v.return_variation()

if __name__ == '__main__':
    main(sys.argv[1:])