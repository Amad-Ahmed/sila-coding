from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.department import Department
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from models.student_course import StudentCourse
from models.teacher_course import TeacherCourse
from datetime import date

def seed_data():
    # create a new database session
    db = SessionLocal()
    # start a new transaction
    with db.begin():
        # check if data already exists to avoid re-seeding
        if db.query(Department).count() == 0:
            # seed departments
            math_dept = Department(name="Mathematics")
            db.add(math_dept)

            # seed courses
            algebra_course = Course(title="Algebra I", description="Basic Algebra Course", credits=4, dept_id=math_dept.id)
            db.add(algebra_course)

            # seed students
            student_john = Student(name="John Doe", dob=date(2000, 1, 1), dept_id=math_dept.id)
            db.add(student_john)

            # seed teachers
            teacher_jane = Teacher(name="Jane Smith", dept_id=math_dept.id)
            db.add(teacher_jane)


            # seed student_course
            student_course_record = StudentCourse(student_id=student_john.id, course_id=algebra_course.id)
            db.add(student_course_record)

            # seed teacher_course
            teacher_course_record = TeacherCourse(teacher_id=teacher_jane.id, course_id=algebra_course.id)
            db.add(teacher_course_record)

            # final commit for all additions
            db.commit()
            print("Database seeded successfully.")

# Close the session
    db.close()
