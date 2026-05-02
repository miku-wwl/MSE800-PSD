-- Week 3 - Activity 1.1
-- 常用查询示例

PRAGMA foreign_keys = ON;

-- 1) 查看所有学生
SELECT * FROM student;

-- 2) 查看所有课程
SELECT * FROM course;

-- 3) 查看某个学生选了哪些课
-- 把 1 换成你要查询的 student_id
SELECT
  s.student_id,
  s.first_name,
  s.last_name,
  c.course_code,
  c.course_name,
  e.enrolled_on,
  e.status,
  e.grade
FROM enrollment e
JOIN student s ON s.student_id = e.student_id
JOIN course  c ON c.course_id  = e.course_id
WHERE s.student_id = 1
ORDER BY c.course_code;

-- 4) 查看某门课程有哪些学生
-- 把 'MSE800' 换成你要查询的 course_code
SELECT
  c.course_code,
  c.course_name,
  s.student_id,
  s.first_name,
  s.last_name,
  e.status
FROM enrollment e
JOIN student s ON s.student_id = e.student_id
JOIN course  c ON c.course_id  = e.course_id
WHERE c.course_code = 'MSE800'
ORDER BY s.last_name, s.first_name;
