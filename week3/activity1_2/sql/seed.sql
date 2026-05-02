-- Week 3 - Activity 1.2
-- 初始化数据 (可选)

PRAGMA foreign_keys = ON;

-- 先插入讲师（主管为空）
INSERT INTO lecturer (full_name, email, hire_date, office_room, manager_lecturer_id)
VALUES
('Dr. Chen', 'chen@example.com', '2021-02-01', 'B-201', NULL),
('Ms. Li',   'li@example.com',   '2022-03-15', 'B-105', 1);

INSERT INTO student (first_name, last_name, email, date_of_birth)
VALUES
('Alice', 'Wang', 'alice@example.com', '2000-01-01'),
('Bob', 'Zhang', 'bob@example.com', '1999-05-20');

INSERT INTO course (course_code, course_name, credits, lecturer_id)
VALUES
('MSE800', 'Professional Software Engineering', 15, 1),
('MSE801', 'Software Architecture', 15, 2);

INSERT INTO enrollment (student_id, course_id, status)
VALUES
(1, 1, 'enrolled'),
(1, 2, 'enrolled'),
(2, 1, 'enrolled');
