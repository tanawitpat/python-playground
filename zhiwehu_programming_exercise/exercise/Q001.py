import unittest

"""
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""

def logic(lower, upper):
    output = []
    for i in range(lower, upper+1):
        if i % 7 == 0 and i % 5 != 0:
            output.append(i)
    return output

class TestLogic(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(logic(20,30), [21,28], "Should be 21 and 28")
        self.assertEqual(logic(40,70), [42,49,56,63], "Should be 42, 49, 56, and 63")
        self.assertEqual(logic(70,84), [77,84], "Should be 77 and 84")

if __name__ == '__main__':
    unittest.main()