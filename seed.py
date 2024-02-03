from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.department import Department
from models.course import Course
from models.student import Student
from models.teacher import Teacher
from models.student_course import StudentCourse
from models.teacher_course import TeacherCourse
from datetime import datetime

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
            physics_dept = Department(name="Physics")
            db.add(physics_dept)
            chemistry_dept = Department(name="Chemistry")
            db.add(chemistry_dept)
            biology_dept = Department(name="Biology")
            db.add(biology_dept)

            # seed courses
            algebra_course = Course(title="Algebra I", description="Basic Algebra Course", credits=4, dept_id=math_dept.id)
            db.add(algebra_course)
            geometry_course = Course(title="Geometry I", description="Basic Geometry Course", credits=4, dept_id=math_dept.id)
            db.add(geometry_course)
            quantum_course = Course(title="Quantum Mechanics", description="Advanced Quantum Mechanics", credits=4, dept_id=physics_dept.id)
            db.add(quantum_course)
            thermo_course = Course(title="Thermodynamics", description="Advanced Thermodynamics", credits=4, dept_id=physics_dept.id)
            db.add(thermo_course)
            organic_chem_course = Course(title="Organic Chemistry", description="Advanced Organic Chemistry", credits=4, dept_id=chemistry_dept.id)
            db.add(organic_chem_course)
            inorganic_chem_course = Course(title="Inorganic Chemistry", description="Advanced Inorganic Chemistry", credits=4, dept_id=chemistry_dept.id)
            db.add(inorganic_chem_course)
            genetics_course = Course(title="Genetics", description="Advanced Genetics", credits=4, dept_id=biology_dept.id)
            db.add(genetics_course)
            botany_course = Course(title="Botany", description="Advanced Botany", credits=4, dept_id=biology_dept.id)
            db.add(botany_course)

            # seed students
            student_john = Student(name="John Doe", dob=datetime(2000, 1, 1), dept_id=math_dept.id)
            db.add(student_john)
            student_jane = Student(name="Jane Smith", dob=datetime(2000, 1, 1), dept_id=chemistry_dept.id)
            db.add(student_jane)
            student_joe = Student(name="Joe Brown", dob=datetime(2000, 1, 1), dept_id=physics_dept.id)
            db.add(student_joe)
            student_alex = Student(name="Alex Johnson", dob=datetime(2000, 1, 1), dept_id=biology_dept.id)
            db.add(student_alex)

            # seed teachers
            teacher_roscoe = Teacher(name="Roscoe Smith", dept_id=math_dept.id)
            db.add(teacher_roscoe)
            teacher_john = Teacher(name="John Doe", dept_id=biology_dept.id)
            db.add(teacher_john)
            teacher_joe = Teacher(name="Joe Brown", dept_id=physics_dept.id)
            db.add(teacher_joe)
            teacher_alex = Teacher(name="Alex Johnson", dept_id=chemistry_dept.id)
            db.add(teacher_alex)


            # seed student_course
            student_course_record = StudentCourse(student_id=student_john.id, course_id=algebra_course.id)
            db.add(student_course_record)
            student_course_record = StudentCourse(student_id=student_jane.id, course_id=organic_chem_course.id)
            db.add(student_course_record)
            student_course_record = StudentCourse(student_id=student_joe.id, course_id=quantum_course.id)
            db.add(student_course_record)

            # seed teacher_course
            teacher_course_record = TeacherCourse(teacher_id=teacher_roscoe.id, course_id=algebra_course.id)
            db.add(teacher_course_record)
            teacher_course_record = TeacherCourse(teacher_id=teacher_john.id, course_id=botany_course.id)
            db.add(teacher_course_record)
            teacher_course_record = TeacherCourse(teacher_id=teacher_joe.id, course_id=thermo_course.id)
            db.add(teacher_course_record)

            # final commit for all additions
            db.commit()
            print("Database seeded successfully.")

# Close the session
    db.close()
