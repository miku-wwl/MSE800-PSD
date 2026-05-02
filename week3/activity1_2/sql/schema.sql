-- Week 3 - Activity 1.2
-- 在 Activity 1.1 基础上新增 Lecturer 实体，并包含 PK/FK。
-- 这里使用自关联 FK：LECTURER.manager_lecturer_id -> LECTURER.lecturer_id
-- 同时让 COURSE 关联 lecturer_id (FK)。

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS lecturer (
    lecturer_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name            TEXT NOT NULL,
    email                TEXT NOT NULL UNIQUE,
    hire_date            TEXT,
    office_room          TEXT,
    manager_lecturer_id  INTEGER,

    FOREIGN KEY (manager_lecturer_id) REFERENCES lecturer(lecturer_id)
);

CREATE TABLE IF NOT EXISTS student (
    student_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,
    email           TEXT NOT NULL UNIQUE,
    date_of_birth   TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS course (
    course_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code     TEXT NOT NULL UNIQUE,
    course_name     TEXT NOT NULL,
    credits         INTEGER NOT NULL,
    lecturer_id     INTEGER NOT NULL,
    is_active       INTEGER NOT NULL DEFAULT 1,

    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id)
);

CREATE TABLE IF NOT EXISTS enrollment (
    enrollment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id      INTEGER NOT NULL,
    course_id       INTEGER NOT NULL,
    enrolled_on     TEXT NOT NULL DEFAULT (date('now')),
    status          TEXT NOT NULL DEFAULT 'enrolled',
    grade           TEXT,

    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
);
