USE college_db;

-- Task 1

EXPLAIN
SELECT s.first_name,
s.last_name,
c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Observation:
-- Table scan found on students table.
-- Estimated rows examined: 10.

-- Task 2

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id, course_id);

CREATE INDEX idx_course_code
ON courses(course_code);

EXPLAIN
SELECT s.first_name,
s.last_name,
c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Observation:
-- Indexes already exist.
-- Duplicate key name errors confirm the indexes were previously created.

-- Partial indexes are not supported in MySQL.

-- Task 3

-- N+1 Query Problem:
-- 1 query retrieves enrollments.
-- Additional queries retrieve related student data.

-- JOIN Solution:
-- A single JOIN query retrieves all enrollment and student data.

-- If there are 10000 enrollments:
-- N+1 approach executes 10001 queries.
-- JOIN approach executes only 1 query.
