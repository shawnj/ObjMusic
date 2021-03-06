from .tools import *
from .midi import *
import sys
import random
#import midiutil
import mido
import math

def convert_midi(note,tpb):
    octave = random.sample(range(3,6),1)[0]
    __retr_note = note_name_to_number(note.split(":")[0]+str(octave))
    __retr_time = 1/int(note.split(":")[1])*tpb
    return list([__retr_note,__retr_time])

def transfer_midi(variation,out_path):
    __time = 0
    #__tempo = mido.bpm2tempo(bpm)
    #__octave = octave

    ticks_per_beat = 960

   # mido.MetaMessage('set_tempo', tempo=__tempo)

    outfile = mido.MidiFile()
    track = mido.MidiTrack()
    outfile.tracks.append(track)

    for x in variation:
        __velocity = random.sample(range(85,110),1)[0]
        __tmp = convert_midi(x,ticks_per_beat)
        __note = __tmp[0]
        __time = int(__tmp[1])
        
        #print (__time,__note)
        track.append(mido.Message('note_on',note=__note,velocity=__velocity, time=__time))
        track.append(mido.Message('note_off',note=__note,velocity=__velocity, time=__time))

    track.append(mido.Message('note_on',note=60,velocity=0, time=240))
    track.append(mido.Message('note_off',note=60,velocity=0, time=240))

    outfile.save(out_path)

def main(args):

    #KEY = random.sample(list(Notes().notes().keys()),1)[0]
    KEY = args[0]
    SCALE = args[1]
    PITCH_X = args[2]
    PITCH_Y = args[3]
    TIME_SET = args[4]
    TIME_X = args[5]
    TIME_Y = args[6]
    NUM_NOTES = args[7]
    OUT_PATH = args[8]
    #OCTAVE = args[9]
    #BPM = args[10]
    
    __p = PitchSet(SCALE,KEY,PITCH_X,PITCH_Y).get_grid()
    __t = TimeSet(TIME_SET,TIME_X,TIME_Y).get_grid()
    __o = OrderSet(NUM_NOTES).get_order()
    __v = Variation(__o,__p,__t)

    transfer_midi(__v.return_variation(),OUT_PATH)

    return __v.return_variation()

if __name__ == '__main__':
    main(sys.argv[1:])