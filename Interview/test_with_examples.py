import unittest
import json
from main import Solution


class TestExamples(unittest.TestCase):
    def test_eg1(self):
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output1.json'
        ]
        ex_dir = './Example1/{}'
        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()
        self.assertEqual(..., json.load(ex_dir.format('output.json')))


if __name__ == '__main__':
    unittest.main()
