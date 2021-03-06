import sys
sys.path.append('../../tests')
sys.path.append('../../')
from testUtils import *

class Complex:
    def __init__(self, realpart, imagpart, special = "not special"):
        self.realpart = realpart
        self.imagpart = imagpart
        self.special = special
    def __str__(self):
         return ("%s Is the special oF %di + %d" % (self.special, self.realpart, self.imagpart))


fullTest(readFile("ex_01_input.txt"), readFile("ex_01_parser.txt"), "Example 01", expectedCountVars = 17, classes= [Complex], debugPrint = True)