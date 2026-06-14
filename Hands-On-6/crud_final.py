"""
TASK 3: N+1 QUERY ANALYSIS

Without joinedload():
SQLAlchemy executes one query for enrollments and
additional queries for related student and course data.

With joinedload():
Enrollment, Student, and Course data are fetched
using a single JOIN query.

This eliminates the N+1 query problem and improves performance.
"""
from sqlalchemy.orm import sessionmaker, joinedload

from models import (
    engine,
    Student,
    Enrollment,
    Course
)

Session = sessionmaker(bind=engine)
session = Session()

# --------------------
# READ
# --------------------

print("\nALL STUDENTS\n")

students = session.query(Student).all()

for s in students:
    print(
        s.student_id,
        s.first_name,
        s.last_name,
        s.email
    )

# --------------------
# UPDATE
# --------------------

student = (
    session.query(Student)
    .filter(
        Student.email == "arjun.orm@gmail.com"
    )
    .first()
)

if student:
    student.enrollment_year = 2025
    session.commit()
    print("\nUPDATE SUCCESSFUL")

# --------------------
# DELETE
# --------------------

enrollment = (
    session.query(Enrollment)
    .first()
)

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("DELETE SUCCESSFUL")

# --------------------
# N+1 FIX USING JOINEDLOAD
# --------------------

print("\nJOINEDLOAD DEMO\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )