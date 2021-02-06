import csv, json, sys
from collections import defaultdict


class Solution:
    def __init__(self, files):
        self.courses_file = files[0]
        self.students_file = files[1]
        self.tests_file = files[2]
        self.marks_file = files[3]
        self.output_file = files[4]
    
    def loading(self):
        self.courses = {}
        with open(self.courses_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = row['id']
                self.courses[key] = row

        self.students = {}
        with open(self.students_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = row['id']
                self.students[key] = row

        self.tests = {}
        with open(self.tests_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = row['id']
                self.tests[key] = row
        
        self.marks = defaultdict(list)
        with open(self.marks_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = row['student_id']
                self.marks[key].append(row)

    def combining(self):
        self.loading()
        marks = self.marks
        d = []
        for i in marks:
            cur = {'id': int(i), 'name': self.students[i]['name']}
            cur_avg = 0
            cur_c = {}
            for t in marks[i]:
                test = self.tests[t['test_id']]
                c_i = test['course_id']
                c_w = test['weight']

                if c_i not in cur_c:
                    tmp = self.courses[c_i]
                    # TODO check total weights is 100 
                    tmp['courseAverage'] = int(t['mark']) * int(c_w) / 100
                else:
                    cur_c[c_i]['courseAverage'] = 0
            
            cur['totalAverage'] = cur_avg
            cur['courses'] = cur_c
            d.append(cur)
        
        return d
    
    def writing(self):
        res = self.combining()
        json.dumps(res)


testing_files = ['courses.csv', 'students.csv', 'tests.csv', 'marks.csv', 'output1.json']
test1_dir = './Example1/'
test2_dir = './Example2/'
sol = Solution([test1_dir + s for s in testing_files])
sol.combining()


# if __name__ == '__main__':
#     sol = Solution(sys.argv[1:6])
    