import sys
import os

class Intervals(object):

    def __init__(self, I1,I2,I3,I4,I5,I6,I7):
        self.I1 = I1
        self.I2 = I2
        self.I3 = I3
        self.I4 = I4
        self.I5 = I5
        self.I6 = I6
        self.I7 = I7

class Scales(object):

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

        __scale = [x for x in self.scales().items() if scale in x]

        return dict(__scale)[scale]

class Notes(object):

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
            "B": 12
        }

        return __notes

class PitchSet(object):

    def __init__(self, paramer):
        pass

class TimeSet(object):

    def __init__(self, parameter_list):
        pass



