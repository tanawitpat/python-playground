import unittest

'''
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def logic(input_number):
    output = input_number
    for i in range(1,input_number):
        output = output*i
    return output

## Solution
def fact(input_number): 
    if input_number == 0:
        return 1
    return input_number * fact(input_number-1)

class TestLogic(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(logic(8), 40320, "Should be 40320")
        self.assertEqual(logic(1), 1, "Should be 1")

    def test_fact(self):
        self.assertEqual(fact(8), 40320, "Should be 40320")
        self.assertEqual(fact(1), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()