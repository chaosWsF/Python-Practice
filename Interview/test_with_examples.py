import unittest
import json
from main import Solution


class TestExamples(unittest.TestCase):
    def test_eg1(self):
        ex_dir = './Example1/{}'

        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_1.json'
        ]
        sol = Solution([ex_dir.format(s) for s in ex_files])
        d = sol.combining()
        res = json.dumps({'students': d}, indent=2)

        with open(ex_dir.format('output.json')) as f:
            expected_res = f.read()
        
        self.assertEqual(res, expected_res)
    
    def test_eg2(self):
        ex_dir = './Example2/{}'

        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_1.json'
        ]
        sol = Solution([ex_dir.format(s) for s in ex_files])
        d = sol.combining()
        res = json.dumps({'students': d}, indent=2)

        with open(ex_dir.format('output.json')) as f:
            expected_res = f.read()
        
        self.assertEqual(res, expected_res)


if __name__ == '__main__':

    # TestExamples().test_eg1()
    # TestExamples().test_eg2()

    unittest.main()
