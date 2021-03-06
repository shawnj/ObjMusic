import sys
import os
import random
import operator

from .midi import *

class Intervals:

    def __init__(self, I1,I2,I3,I4,I5,I6,I7):
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
        self.I5 = I5
        self.I6 = I6
        self.I7 = I7

class Scales:

    def __init__(self):
        self.scale = "Major"

    def scales(self):
        __scales = {
            "Major": (2, 2, 1, 2, 2, 2, 1),
            "Minor": (2, 1, 2, 2, 1, 2, 2),
            "Dorian": (2, 1, 2, 2, 2, 1, 2),
            "Phrygian": (1, 2, 2, 2, 1, 2, 2),
            "Lydian": (2, 2, 2, 1, 2, 2, 1),
            "MixoLydian": (2, 2, 1, 2, 2, 1, 2),
            "Locrian": (1, 2, 2, 1, 2, 2, 2),
            "Melodic": (2, 1, 2, 2, 2, 2, 1),
            "Dorian #2": (1, 2, 2, 2, 2, 1, 2),
            "Lydian Aug": (2, 2, 2, 2, 1, 2, 1),
            "Lydian Dom": (2, 2, 2, 1, 2, 1, 2),
            "Hindu": (2, 2, 1, 2, 1, 2, 2),
            "Locrian Nat. 2": (2, 1, 2, 1, 2, 2, 2),
            "Super Locrian": (1, 2, 1, 2, 2, 2, 2),
            "Harmonic Minor": (2, 1, 2, 2, 1, 3, 1),
            "Locrian Nat 6": (1, 2, 2, 1, 3, 1, 2),
            "Ionion #5": (2, 2, 1, 3, 1, 2, 1),
            "Dorian #4": (2, 1, 3, 1, 2, 1, 2),
            "Phyrgian Nat 3": (1, 3, 1, 2, 1, 2, 2),
            "Lydian #2": (3, 1, 2, 1, 2, 2, 1),
            "Alt bb7": (1, 2, 1, 2, 2, 1, 3),
            "Harmonic Major": (2, 2, 1, 2, 1, 3, 1),
            "Dorian b5": (2, 1, 2, 1, 3, 1, 2),
            "Phyrgian b4": (1, 2, 1, 3, 1, 2, 2),
            "Lydian  b3": (2, 1, 3, 1, 2, 2, 1),
            "Dominant  b2": (1, 3, 1, 2, 2, 1, 2),
            "Lydian Aug #2": (3, 1, 2, 2, 1, 2, 1),
            "Locrian bb 7": (1, 2, 2, 1, 2, 1, 3),
            "Hungarian Minor": (2, 1, 3, 1, 1, 3, 1),
            "Oriental 2": (1, 3, 1, 1, 3, 1, 2),
            "Ionian Aug #2": (3, 1, 1, 3, 1, 2, 1),
            "Locrian bb3 bb7": (1, 1, 3, 1, 2, 1, 3),
            "Double Harmonic": (1, 3, 1, 2, 1, 3, 1),
            "Lydian #6 #2": (3, 1, 2, 1, 3, 1, 1),
            "Alt Nat 5 bb7": (1, 2, 1, 3, 1, 1, 3),
            "Hungarian Major": (3, 1, 2, 1, 2, 1, 2),
            "Alt bb6 bb7": (1, 2, 1, 2, 1, 2, 3),
            "Locrian N2 N7": (2, 1, 2, 1, 2, 3, 1),
            "Alt N6": (1, 2, 1, 2, 3, 1, 2),
            "Melodic Aug": (2, 1, 2, 3, 1, 2, 1),
            "Dorian b2 #4": (1, 2, 3, 1, 2, 1, 2),
            "Lydian Aug #3": (2, 3, 1, 2, 1, 2, 1),
            "Neopolitan Minor": (1, 2, 2, 2, 1, 3, 1),
            "Lydian #6": (2, 2, 2, 1, 3, 1, 1),
            "Dom Aug": (2, 2, 1, 3, 1, 1, 2),
            "Hungarian Gypsy": (2, 1, 3, 1, 1, 2, 2),
            "Locrian N3": (1, 3, 1, 1, 2, 2, 2),
            "Ionian #2": (3, 1, 1, 2, 2, 2, 1),
            "Alt bb3 bb7": (1, 1, 2, 2, 2, 1, 3),
            "Neopolitan Major": (1, 2, 2, 2, 2, 2, 1),
            "Lydian Aug #6": (2, 2, 2, 2, 2, 1, 1),
            "Lydian Dom Aug": (2, 2, 2, 2, 1, 1, 2),
            "Lydian Minor": (2, 2, 2, 1, 1, 2, 2),
            "Major Locrian": (2, 2, 1, 1, 2, 2, 2),
            "Alt N2": (2, 1, 1, 2, 2, 2, 2),
            "Alt #3": (1, 1, 2, 2, 2, 2, 2),
            "Enigmatic Minor": (1, 2, 3, 1, 3, 1, 1),
            "Enigmatic Minor Mode 2": (2, 3, 1, 3, 1, 1, 1),
            "Enigmatic Minor Mode 3": (3, 1, 3, 1, 1, 1, 2),
            "Enigmatic Minor Mode 4": (1, 3, 1, 1, 1, 2, 3),
            "Enigmatic Minor Mode 5": (3, 1, 1, 1, 2, 3, 1),
            "Enigmatic Minor Mode 6": (1, 1, 1, 2, 3, 1, 3),
            "Enigmatic Minor Mode 7": (1, 1, 2, 3, 1, 3, 1),
            "Enigmatic": (1, 3, 2, 2, 2, 1, 1),
            "Enigmatic Mode 2": (3, 2, 2, 2, 1, 1, 1),
            "Enigmatic Mode 3": (2, 2, 2, 1, 1, 1, 3),
            "Enigmatic Mode 4": (2, 2, 1, 1, 1, 3, 2),
            "Enigmatic Mode 5": (2, 1, 1, 1, 3, 2, 2),
            "Enigmatic Mode 6": (1, 1, 1, 3, 2, 2, 2),
            "Enigmatic Mode 7": (1, 1, 3, 2, 2, 2, 1),
            "Composite II": (1, 3, 2, 1, 1, 3, 1),
            "Composite II Mode 2": (3, 2, 1, 1, 3, 1, 1),
            "Composite II Mode 3": (2, 1, 1, 3, 1, 1, 3),
            "Composite II Mode 4": (1, 1, 3, 1, 1, 3, 2),
            "Composite II Mode 5": (1, 3, 1, 1, 3, 2, 1),
            "Composite II Mode 6": (3, 1, 1, 3, 2, 1, 1),
            "Composite II Mode 7": (1, 1, 3, 2, 1, 1, 3),
            "Ionian b5": (2, 2, 1, 1, 3, 2, 1),
            "Dorian b4": (2, 1, 1, 3, 2, 1, 2),
            "Phygrian bb3": (1, 1, 3, 2, 1, 2, 2),
            "Lydian b2": (1, 3, 2, 1, 2, 2, 1),
            "Super Lydian Aug": (3, 2, 1, 2, 2, 1, 1),
            "Aeolian bb7": (2, 1, 2, 2, 1, 1, 3),
            "Locrian b6": (1, 2, 2, 1, 1, 3, 2),
            "Locrian N7": (1, 2, 2, 1, 2, 3, 1),
            "Ionian #8": (2, 2, 1, 2, 3, 1, 1),
            "Dorian Aug": (2, 1, 2, 3, 1, 1, 2),
            "Phygrian #4": (1, 2, 3, 1, 1, 2, 2),
            "Lydian #3": (2, 3, 1, 1, 2, 2, 1),
            "Dominant #2": (3, 1, 1, 2, 2, 1, 2),
            "Alt Alt": (1, 1, 2, 2, 1, 2, 3),
            "Persian": (1, 3, 1, 1, 2, 3, 1),
            "Persian Mode 2": (3, 1, 1, 2, 3, 1, 1),
            "Persian Mode 3": (1, 1, 2, 3, 1, 1, 3),
            "Persian Mode 4": (1, 2, 3, 1, 1, 3, 1), 
            "Persian Mode 5": (2, 3, 1, 1, 3, 1, 1),
            "Persian Mode 6": (3, 1, 1, 3, 1, 1, 2),
            "Persian Mode 7": (1, 1, 3, 1, 1, 2, 3)
        }

        return __scales

    def get_scale(self, scale):
        self.scale = scale
        __scale = [x for x in self.scales().items() if self.scale in x]

        return dict(__scale)[self.scale]

class TimeValues:

    def __init__(self):
        self.tv = "One"
        self.timeset = (2,4,2,4,2,4,2)

    def tvs(self):
        __tvs = {
            "One": (2, 4, 2, 4, 4, 2, 4),
            "Two": (4, 8, 4, 8, 2, 4, 8),
            "Three": (8, 16, 8, 16, 16, 8, 16),
            "Four": (2,4,2,4,8,2,8)
        }

        return __tvs

    def get_tv(self, tv):
        self.tv = tv
        __tvs = [x for x in self.tvs().items() if self.tv in x]

        return dict(__tvs)[self.tv]
    
    def get_timeset(self,timeset):
        self.timeset = eval(timeset)

        return self.timeset
        
class Notes:

    def notes(self):
        __notes = {
            "C": 1,
            "C#": 2,
            "D": 3,
            "D#": 4,
            "E": 5,
            "F": 6,
            "F#": 7,
            "G": 8,
            "G#": 9,
            "A": 10,
            "A#": 11,
            "B": 0
        }

        return __notes

class MidiNotes:

    def midi_notes(self):

        __m_notes = {

        }

        return __m_notes
    
class PitchSet:

    def __init__(self,scale,rootnote,x,y):
        self.scale = scale
        self.rootnote = rootnote
        self.x = x
        self.y = y
    
    def get_grid(self):
        __notes = load_notes(self.scale,self.rootnote)
        return populate_grid(__notes,self.x,self.y)

class TimeSet:

    def __init__(self,timevalue,x,y):
        self.x = x
        self.y = y
        self.timevalue = timevalue
        #self.positions = list(positions)
    
    #positions = property(operator.attrgetter('_positions'))
    
    #@positions.setter
    #def positions(self,p):
    #    if len(p) != 7: raise Exception("Length of Time inputs not 7.")
    #    self._positions = p

    def get_grid(self):
        __timevalues = load_timevalues(self.timevalue)
        return populate_grid(__timevalues,self.x,self.y)

    def get_gridset(self):
        __timevalues = load_timeset(self.timevalue)
        return populate_grid(__timevalues,self.x,self.y)

class OrderSet:

    def __init__(self,num_notes):
        self.num_notes = num_notes

    def get_order(self):
        __num_notes = self.num_notes
        __r = random.sample(range(0,63), int(__num_notes))
        return __r

class Variation:
    
    def __init__(self, order_set,pitch_set,time_set):
        self.order_set = order_set
        self.pitch_set = pitch_set
        self.time_set = time_set
    
    def return_variation(self):
        __var = []

        for x in self.order_set:
            p = self.pitch_set[int(x)]
            t = self.time_set[int(x)]
            s = str(str(p)+":"+str(t))
            __var.append(s)

        return __var

## Methods
def populate_grid(item_list,x,y):
    __l = []
    inc = 0
    index = 0

    for p in range(8):
        inc2 = 0
        for i in range(7):
            if i == 0:
                inc2 = inc
            __l.insert(index,item_list[inc])
            inc = (inc + int(x) - 1) % 7
            index += 1

        index += 1
        __l.insert(index,item_list[inc2])
        inc = (inc + int(y) -1) % 7

    return __l
    

def load_scale(scale):
    __scale = Scales().get_scale(scale)
    __intervals = ""

    if len(__scale) == 7:
        __intervals = Intervals(__scale[0],__scale[1],__scale[2],__scale[3],__scale[4],__scale[5],__scale[6])

    __loaded_s = __intervals 

    return __loaded_s

def load_notes(scale, rootnote):
    __ls = load_scale(scale)
    __notes = Notes().notes()
    __root = __notes[rootnote.upper()]

    note_num = list()

    note_num.append(__root)
    note_num.append((note_num[0]+__ls.I1)%12)
    note_num.append((note_num[1]+__ls.I2)%12)
    note_num.append((note_num[2]+__ls.I3)%12)
    note_num.append((note_num[3]+__ls.I4)%12)
    note_num.append((note_num[4]+__ls.I5)%12)
    note_num.append((note_num[5]+__ls.I6)%12)
    note_num.append((note_num[6]+__ls.I7)%12)

    convert_notes = list()

    for x in note_num:
        note = [i[0] for i in __notes.items() if x in i]
        convert_notes.append(note[0])

    return convert_notes

# Not currently using
def load_timevalues(timevalue):
    __tv = TimeValues().get_tv(timevalue)
    __loaded_tv = __tv

    return __loaded_tv

def load_timeset(timeset):
    __tv = TimeValues().get_timeset(timeset)

    return __tv
