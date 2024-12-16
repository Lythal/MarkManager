import sqlite3
from contextlib import contextmanager

con = sqlite3.connect("courses.db")
cursor = con.cursor()

# SOME SOLUTION
# @contextmanager
# def getCon():
#     con = sqlite3.connect("courses.db")
#     try:
#         yield con
#     finally:
#         con.close()

def addCourse(courseCode, courseTitle):
    cursor.execute("INSERT INTO courses(code, title) VALUES (?, ?);", (courseCode, courseTitle))
    con.commit()

def dropCourse(courseCode):
    cursor.execute("DELETE FROM courses WHERE code = ?;", (courseCode,))
    con.commit()

def renameCourse(course, newCode, newTitle):
    cursor.execute("UPDATE courses SET code = ?, title = ? WHERE code = ?;", (newCode, newTitle, course))
    con.commit()

def addAssessment(course, name, mark, weight):
    cursor.execute("INSERT INTO assessments(code, name, mark, weight) VALUES(?, ?, ?, ?);", (course, name, mark, weight))
    con.commit()

def dropAssessment(name):
    cursor.execute("DELETE FROM assessments WHERE name=?;", (name,))
    con.commit()

def renameAssessment(course, current, new):
    cursor.execute("UPDATE assessments SET name = ? WHERE code = ?, name = ?", (new, course, current))
    con.commit()

def editAssessment(course, name, newMark, newWeight):
    cursor.execute("UPDATE assessments SET mark = ?, weight = ? WHERE code = ? AND name = ?;", (newMark, newWeight, course, name))
    con.commit()

def updateCourseAverages():
    cursor.execute("SELECT code FROM courses;")
    numCourses = cursor.fetchall()
    for course in numCourses:
        courseCode = course[0]
        cursor.execute("SELECT SUM(mark * weight) / SUM(weight) AS weightedAverage FROM assessments WHERE code = ?;", (courseCode,))
        result = cursor.fetchone()
        if result[0] is not None:
            weightedAverage = round(result[0], 1)
            cursor.execute("UPDATE courses SET average = ? WHERE code = ?;", (weightedAverage, courseCode))
            con.commit()

def editSemester(course, current, new):
    cursor.execute("UPDATE courses SET semester = ? WHERE code = ? AND semester = ?;", (new, course, current))
    con.commit()

def fetchCourses():
    cursor.execute("SELECT * FROM courses;")
    return cursor.fetchall()

def fetchAssessments(course):
    cursor.execute("SELECT name, mark, weight FROM assessments WHERE code = ?", (course,))
    return cursor.fetchall()

def closeCon():
    con.close()
#testing
print(fetchCourses())

