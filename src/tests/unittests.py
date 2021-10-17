import unittest, os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, parentdir)

from Affirmations import affirm
from Affirmations.AffirmationText import affirmations

class testAffirmDecorator(unittest.TestCase):
    def setUp(self):
        pass

    def test_isString(self):
        pass

    def test_isList(self):
        pass

    

    def tearDown(self):
        pass

if __name__=="__main__":
    print(affirmations[-1])
    print(sys.path)