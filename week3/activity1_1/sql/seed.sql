-- Week 3 - Activity 1.1
-- 初始化数据 (可选)

PRAGMA foreign_keys = ON;

INSERT INTO student (first_name, last_name, email, date_of_birth)
VALUES
('Alice', 'Wang', 'alice@example.com', '2000-01-01'),
('Bob', 'Zhang', 'bob@example.com', '1999-05-20');

INSERT INTO course (course_code, course_name, credits, level)
VALUES
('MSE800', 'Professional Software Engineering', 15, 'PG'),
('MSE801', 'Software Architecture', 15, 'PG');

-- enroll Alice in both courses
INSERT INTO enrollment (student_id, course_id, status)
VALUES
(1, 1, 'enrolled'),
(1, 2, 'enrolled');

-- enroll Bob in MSE800
INSERT INTO enrollment (student_id, course_id, status)
VALUES
(2, 1, 'enrolled');
