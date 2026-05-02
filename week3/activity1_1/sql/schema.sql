-- Week 3 - Activity 1.1
-- 学生与课程：数据库表结构 (SQLite)
-- 说明：学生与课程是 M:N，用 ENROLLMENT 中间表实现。

PRAGMA foreign_keys = ON;

-- 学生表
CREATE TABLE IF NOT EXISTS student (
    student_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    date_of_birth   TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

-- 课程表
CREATE TABLE IF NOT EXISTS course (
    course_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code     TEXT NOT NULL UNIQUE,
    course_name     TEXT NOT NULL,
    credits         INTEGER NOT NULL,
    level           TEXT,
    is_active       INTEGER NOT NULL DEFAULT 1
);

-- 选课表（中间表）
CREATE TABLE IF NOT EXISTS enrollment (
    enrollment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id      INTEGER NOT NULL,
    course_id       INTEGER NOT NULL,
    enrolled_on     TEXT NOT NULL DEFAULT (date('now')),
    status          TEXT NOT NULL DEFAULT 'enrolled',
    grade           TEXT,

    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,

    -- 防止同一个学生重复选同一门课
    UNIQUE (student_id, course_id)
);
