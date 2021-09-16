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
                key = int(row['id'])
                
                if row['teacher'][0] == ' ':
                    row['teacher'] = row['teacher'][1:]
                
                self.courses[key] = row

        self.students = {}
        with open(self.students_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = int(row['id'])
                self.students[key] = row

        self.tests = defaultdict(list)
        with open(self.tests_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = int(row['course_id'])
                self.tests[key].append(row)
        
        self.marks = {}
        with open(self.marks_file) as f:
            f_reader = csv.DictReader(f)
            for row in f_reader:
                key = (row['test_id'], int(row['student_id']))
                self.marks[key] = row

    def combining(self):
        d = []
        for s_id in self.students:
            tmp = self.students[s_id]
            student = OrderedDict({
                'id': int(tmp['id']),
                'name': tmp['name']
            })
            
            s_courses, gpa = [], []
            for c_id in self.courses:
                tmp = self.courses[c_id]
                course = OrderedDict({
                    'id': int(tmp['id']),
                    'name': tmp['name'],
                    'teacher': tmp['teacher']
                })

                grades = []
                if self.tests.get(c_id) is not None:    # ensure the course has a test
                    for t in self.tests[c_id]:
                        if self.marks.get((t['id'], student['id'])) is not None:    # ensure the student did attend the test
                            score = self.marks[(t['id'], student['id'])]['mark']
                            grades.append(int(score) * int(t['weight']) / 100)
                
                if grades:    # ensure the student takes the course
                    grade = sum(grades)
                    course.update({'courseAverage': round(grade, 2)})
                    s_courses.append(course)
                    gpa.append(grade)

            student.update({"totalAverage": round(sum(gpa) / len(gpa), 2)})
            student.update({"courses": s_courses})
            d.append(student)

        return d
    
    def writing(self):
        self.loading()
        if any([sum([int(t['weight']) for t in ts]) != 100 for ts in self.tests.values()]):
            res = json.dumps({"error": "Invalid course weights"}, indent=2)
        else:
            d = self.combining()
            res = json.dumps({'students': d}, indent=2)
        
        with open(self.output_file, 'w', encoding='utf-8') as fw:
            fw.write(res)


if __name__ == '__main__':
    sol = Solution(sys.argv[1:6])
    sol.writing()
