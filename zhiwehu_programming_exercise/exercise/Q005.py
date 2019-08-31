import unittest

'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class String():
    def __init__(self, input_string):
        self.s = input_string
    
    def upper(self):
        return self.s.upper()

def logic(input_string):
    string_object = String(input_string)
    logic_output = string_object.upper()
    print(logic_output)
    return logic_output

class TestLogic(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(
            logic("OuiOui"), 
            "OUIOUI", 
            "Should be OUIOUI")

if __name__ == '__main__':
    unittest.main()