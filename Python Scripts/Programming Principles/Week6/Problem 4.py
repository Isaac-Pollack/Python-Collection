"""
// String Problem //
Write a program that allows the user to enter the marks of 5 students in 4 courses
Output the highest average marks for students and courses.
"""

grades = []
studentAverage = []
courseAverage = [0, 0, 0, 0]

# INPUTS
for i in range(5):
    grade = input('Student ' + str(i + 1) + ' (courses 1-4): ')
    c = grade.split(' ')  # SPLIT and APPEND IT
    grades.append([int(c[0]), int(c[1]), int(c[2]), int(c[3])])
    studentAverage.append(sum(grades[i]) / 4)  # SUM IT

# SUMMING COURSE TOTALS (Superrrr important indentation)
    for j in range(4):
        courseAverage[j] += int(c[j])

# AVERAGING COURSES
courseAverage[0] = courseAverage[0] / 5
courseAverage[1] = courseAverage[1] / 5
courseAverage[2] = courseAverage[2] / 5
courseAverage[3] = courseAverage[3] / 5

# PRINT RESULTS
print('The highest average mark of students: {:.2f}'.format(max(studentAverage)))
print('The highest average mark of courses: {:.2f}'.format(max(courseAverage)))
