import unittest

'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''

def logic(input_string):
    input_list = input_string.split(",")
    input_tuple = tuple(input_list)
    return {
        "list": input_list,
        "tuple": input_tuple
    }

class TestLogic(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(
            logic("34,67,55,33,12,98"), 
            {
                "list": ['34', '67', '55', '33', '12', '98'], 
                "tuple": ('34', '67', '55', '33', '12', '98')
            }, 
            "Should be ['34', '67', '55', '33', '12', '98'] and ('34', '67', '55', '33', '12', '98')")

if __name__ == '__main__':
    unittest.main()