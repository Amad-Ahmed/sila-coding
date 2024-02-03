from sqlalchemy.orm import Session
from database import SessionLocal
from models.department import Department
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from models.student_course import StudentCourse
from models.teacher_course import TeacherCourse
from datetime import datetime

def seed_data():
    db = SessionLocal()
    try:
        if db.query(Department).count() == 0:
            departments = [
                Department(name="Mathematics"),
                Department(name="Physics"),
                Department(name="Chemistry"),
                Department(name="Biology")
            ]
            db.add_all(departments)
            db.flush()

            dept_ids = {dept.name: dept.id for dept in departments}

            courses = [
                Course(title="Algebra I", description="Basic Algebra Course", credits=4, dept_id=dept_ids["Mathematics"]),
                Course(title="Geometry I", description="Basic Geometry Course", credits=4, dept_id=dept_ids["Mathematics"]),
                Course(title="Quantum Mechanics", description="Advanced Quantum Mechanics", credits=4, dept_id=dept_ids["Physics"]),
                Course(title="Thermodynamics", description="Advanced Thermodynamics", credits=4, dept_id=dept_ids["Physics"]),
                Course(title="Organic Chemistry", description="Advanced Organic Chemistry", credits=4, dept_id=dept_ids["Chemistry"]),
                Course(title="Inorganic Chemistry", description="Advanced Inorganic Chemistry", credits=4, dept_id=dept_ids["Chemistry"]),
                Course(title="Genetics", description="Advanced Genetics", credits=4, dept_id=dept_ids["Biology"]),
                Course(title="Botany", description="Advanced Botany", credits=4, dept_id=dept_ids["Biology"])
            ]
            db.add_all(courses)
            db.flush()

            course_ids = {course.title: course.id for course in courses}

            students = [
                Student(name="John Doe", dob=datetime(2000, 1, 1), dept_id=dept_ids["Mathematics"]),
                Student(name="Jane Smith", dob=datetime(2000, 1, 1), dept_id=dept_ids["Chemistry"]),
                Student(name="Joe Brown", dob=datetime(2000, 1, 1), dept_id=dept_ids["Physics"]),
                Student(name="Alex Johnson", dob=datetime(2000, 1, 1), dept_id=dept_ids["Biology"])
            ]

            db.add_all(students)
            db.flush()

            student_ids = {student.name: student.id for student in students}

            teachers = [
                Teacher(name="Roscoe Smith", dept_id=dept_ids["Mathematics"]),
                Teacher(name="John Doe", dept_id=dept_ids["Biology"]),
                Teacher(name="Joe Brown", dept_id=dept_ids["Physics"]),
                Teacher(name="Alex Johnson", dept_id=dept_ids["Chemistry"])
            ]

            db.add_all(teachers)
            db.flush()

            teacher_ids = {teacher.name: teacher.id for teacher in teachers}

            student_courses = [
                StudentCourse(student_id=student_ids["John Doe"], course_id=course_ids["Algebra I"]),
                StudentCourse(student_id=student_ids["Jane Smith"], course_id=course_ids["Organic Chemistry"]),
                StudentCourse(student_id=student_ids["Joe Brown"], course_id=course_ids["Quantum Mechanics"]),
                StudentCourse(student_id=student_ids["Alex Johnson"], course_id=course_ids["Botany"])
            ]

            db.add_all(student_courses)
            db.flush()

            teacher_courses = [
                TeacherCourse(teacher_id=teacher_ids["Roscoe Smith"], course_id=course_ids["Algebra I"]),
                TeacherCourse(teacher_id=teacher_ids["John Doe"], course_id=course_ids["Botany"]),
                TeacherCourse(teacher_id=teacher_ids["Joe Brown"], course_id=course_ids["Thermodynamics"]),
                TeacherCourse(teacher_id=teacher_ids["Alex Johnson"], course_id=course_ids["Inorganic Chemistry"])
            ]

            db.add_all(teacher_courses)
            db.commit()
            print("Database seeded successfully.")

    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

