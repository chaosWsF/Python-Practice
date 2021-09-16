import unittest
import json

from main import Solution


class TestExamples(unittest.TestCase):
    def test_eg1(self):
        """
        Test specific fields
        """
        ex_dir = './Example1/{}'
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_test.json'
        ]

        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()

        with open(ex_dir.format(ex_files[-1])) as f:
            res = json.load(f)
        
        with open(ex_dir.format('output.json')) as f:
            expected_res = json.load(f)
            
        self.assertEqual(res['students'][1]['totalAverage'], expected_res['students'][1]['totalAverage'])
        self.assertEqual(res['students'][1]['courses'], expected_res['students'][1]['courses'])
    
    def test_eg2(self):
        """
        Test entire example 2
        """
        ex_dir = './Example2/{}'
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_test.json'
        ]

        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()

        with open(ex_dir.format(ex_files[-1])) as f:
            res = json.load(f)
        
        with open(ex_dir.format('output.json')) as f:
            expected_res = json.load(f)
        
        self.assertEqual(res, expected_res)

    def test_eg3(self):
        """
        Test outputing error when weights are incorrect
        """
        ex_dir = './Example3/{}'
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_test.json'
        ]

        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()

        with open(ex_dir.format(ex_files[-1])) as f:
            res = json.load(f)
        
        self.assertEqual(res, {"error": "Invalid course weights"})


if __name__ == '__main__':
    unittest.main()
