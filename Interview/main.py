import csv, json, sys
from collections import defaultdict, OrderedDict


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

        d = []
        for i in self.marks:
            cur = {'id': int(i), 'name': self.students[i]['name']}
            cur_c = OrderedDict()
            for t_mark in self.marks[i]:
                t = self.tests[t_mark['test_id']]
                c_i = t['course_id']

                if c_i not in cur_c:
                    cur_c[c_i] = self.courses[c_i]
                    cur_c[c_i].update({'courseAverage': []})

                cur_c[c_i]['courseAverage'].append((int(t['weight']), int(t_mark['mark'])))
            
            gpa = []
            for key, val in cur_c.items():
                # check the sum of weights is 100
                if sum([s[0] for s in val['courseAverage']]) == 100:
                    grade = sum([(s[0] * s[1] / 100) for s in val['courseAverage']])
                    cur_c[key]['courseAverage'] = round(grade, 2)
                    gpa.append(grade)
                else:
                    # TODO Output ERROR
                    cur_c[key]['courseAverage'] = 0
            
            cur.update({'totalAverage': round(sum(gpa) / len(gpa), 2)})
            cur.update({'courses': list(cur_c.values())})
            d.append(cur)
        
        return d
    
    def writing(self):
        d = self.combining()
        res = json.dumps({'students': d}, indent=2)
        with open(self.output_file, 'w', encoding='utf-8') as fw:
            fw.write(res)


if __name__ == '__main__':
    sol = Solution(sys.argv[1:6])
    sol.writing()
