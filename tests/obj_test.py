import objmusic
import unittest

def first_num(num):
    return num
class TestObjMusic(unittest.TestCase):

    def test(self):
        self.assertEqual(first_num(1),1)
        
