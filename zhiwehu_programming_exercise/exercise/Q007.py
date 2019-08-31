import unittest

'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''

def logic(x,y):
    dimension_one = []
    for x_element in range(x):
        dimension_two = []
        for y_element in range(y):
            dimension_two.append(x_element*y_element)
        dimension_one.append(dimension_two)
    return dimension_one

class TestLogic(unittest.TestCase):
    def test_logic(self):
        logic_output = logic(3,5)
        print(logic_output)
        self.assertEqual(
            logic_output, 
            [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]], 
            "Should be `[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]`")
            
if __name__ == '__main__':
    unittest.main()