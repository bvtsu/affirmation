import unittest, os, sys, io

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(1, parentdir)
from Affirmations import affirm
from Affirmations.AffirmationText import affirmations

@affirm()
def testFunc():
    return("X")



class testAffirmDecorator(unittest.TestCase):
    def setUp(self):
        pass

    def test_isString(self):
        for item in affirmations:
            self.assertIsInstance(item, str)

    def test_isList(self):
        self.assertIsInstance(affirmations, list)

    def testAffirm(self): # tests it a whole bunch of times to make sure you get outputs
        for _ in range(10000):
            capturedOutput = io.StringIO() 
            sys.stdout = capturedOutput #redirect stdout
            testFunc() # decorated function
            sys.stdout = sys.__stdout__ #put stdout back to normal
            aff = capturedOutput.getvalue() # grab what went to stdout from testFunc

            self.assertIsInstance(aff, str)
            self.assertNotAlmostEqual(len(aff), 0)
        
    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()