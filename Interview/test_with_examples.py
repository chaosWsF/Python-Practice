import unittest
import json
from main import Solution


class TestExamples(unittest.TestCase):
    def test_eg1(self):
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_1.json'
        ]
        ex_dir = './Example1/{}'
        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()
    
    def test_eg2(self):
        ex_files = [
            'courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 
            'output_1.json'
        ]
        ex_dir = './Example2/{}'
        sol = Solution([ex_dir.format(s) for s in ex_files])
        sol.writing()


if __name__ == '__main__':
    # unittest.main()
    TestExamples().test_eg1()
    TestExamples().test_eg2()
