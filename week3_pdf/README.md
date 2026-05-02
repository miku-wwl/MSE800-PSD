# Week 3 Recap (MSE 800)

本目录保存 Week 3 的课件与配套材料。Week 3 的核心主题可以概括为两条线：

- **文件处理 + 模块化**：学会从文件读取真实数据、清洗/抽取信息、输出结果，并用模块/命名空间管理复杂度。
- **数据库连接**：理解数据库/表/SQL 的基础概念，掌握 Python 连接数据库（MySQL/SQLite）并执行 CRUD。

> 备注：本目录里同时出现了 `Week5_1/`（SQLite 用户管理示例）。它来自 `Sample_code_SQLite3.7z`，虽文件夹名写 Week5，但内容与本周 SQLite3 PPTX 高度相关，这里也一并说明。

## Files In This Folder

- week3(a).pdf
  - 主题：File Processing、集合(Set)与 Venn Diagram、模块(Module)、命名空间(Namespace)、全局变量与代码风格（含 Pylint）。

- week3(b)(2).pdf
  - 主题：Python Database Connectivity（以 MySQL 为例）、SQL 基础、Python 连接/建库建表/增删改查、`commit()`、配置文件避免硬编码、练习题。

- SQLite3_Python_Lecture.pptx
  - 主题：SQLite3 in Python（连接、建表、总结与活动）。

- Sample_code_SQLite3.7z
  - SQLite 示例代码压缩包（内容就是 `Week5_1/`）。

- Week5_1/
  - 一个基于 SQLite 的命令行 User Manager 小项目（示例代码见下文）。

- demo_file.txt
  - 一份较大的纯文本文件（Project Gutenberg 电子书内容），适合用于练习“逐行读取、统计、搜索、提取、写出新文件”等文件处理任务。

## Week 3 Learning Outcomes

完成 Week 3 复习后，你应该能做到：

- 熟练使用 `open(path, mode)` 打开文件，理解常见模式：读/写/追加（以及何时需要手动换行符 `\n`）。
- 将文件视为“字符序列”或“行列表”，能写出“逐行处理 + 清洗 + 抽取 + 聚合”的数据处理流程。
- 能从 CSV/日志这类“包含无关信息的真实数据文件”中抽取目标数据（例如通过识别空行、固定行号、分隔符等）。
- 能写出输出文件（例如写 CSV 或写汇总结果），了解 `writelines()` 与写入多行的差异。
- 理解 Set 的四个核心集合运算：`union` / `intersection` / `difference` / `symmetric_difference`。
- 能把代码拆成模块，理解 `import`、`help(module)`、以及 `if __name__ == '__main__':` 的意义。
- 理解命名空间（模块/局部/全局）与 `global` 的使用限制；知道“全局常量 OK，全局变量尽量少用”的规则。
- 理解数据库/表/行/列与 SQL 的 DDL/DML；能用 Python 执行 CRUD；知道 `commit()` 的重要性。
- 知道不要把用户名/密码硬编码在代码里，能用 `.ini` + `configparser` 做配置管理。

## Part A (week3(a).pdf): File Processing + Sets + Modules

### 1) File Processing Basics

课件从“文件处理任务的多样性”切入，给出典型数值数据处理流程（概念上可以总结为）：

1. 打开文件
2. 读取数据（逐行/批量）
3. 清洗/过滤无关行
4. 提取目标字段（split/切片/正则/固定列等）
5. 将字符串转换为数值
6. 聚合计算（sum/mean/max/min…）
7. 输出结果（屏幕或写文件）

关键 API/模式（课件页中有示例代码）：

- `open(path, mode)`：打开文件（Windows 路径可以用正斜杠）。
- `readlines()`：一次性读入所有行成为 list（注意大文件内存问题）。
- 逐行循环处理：`for line in lines:`
- 输出文件：`open('out.txt', 'w')` + 写入字符串；注意通常需要手动包含 `\n`。
- `writelines([...])`：写入多行（不给你自动加换行）。

### 2) Extracting Data From Real Files

真实数据文件常见情况：

- 文件头部包含大量 metadata
- 中间有空行/分隔段
- 某些信息出现在固定行号（如第 7 行是 station name）

课件展示了多种抽取算法思路（例如“找到两行空行之后开始读数据”等），并提出了一个很关键的问题：

- **如果文件不包含预期的两行空行，会发生什么？**

复习时建议你特别关注：

- 输入数据假设（assumptions）要么被验证，要么被容错处理
- 错误信息要可读（不要 silent fail）

### 3) Writing Output Files

课件示例里展示了写文件时常见格式：

- 把多列数据拼成一行（CSV 风格）：`"{0},{1},{2:.3f}\n".format(...)`
- 循环写多行

### 4) Sets + Venn Diagram

Set 的直观理解：用于“去重”和“集合关系运算”。

课件覆盖的核心运算：

- `union`：并集（A 或 B）
- `intersection`：交集（A 且 B）
- `difference`：差集（A 有但 B 没有）
- `symmetric_difference`：对称差（只在其中一个集合中）

### 5) Modules And Imports

- 大程序要拆模块：每个模块聚焦一块功能。
- `import module` 后通过 `module.func()` 使用。
- 学会“找模块里有什么”：
  - 查文档
  - `help(module)`
  - 查看源码（尤其是你自己写的模块）

重点机制：

- 当模块被 `import` 时，模块变量 `__name__` 是模块名
- 当模块作为主程序运行时，`__name__` 会是 `'__main__'`
- 用 `if __name__ == '__main__':` 可以做到：
  - 被 import 时不执行测试代码
  - 自己运行时执行 demo/test

### 6) Namespaces + Globals + Style

- 命名空间可以理解为“名字到对象的字典”。
- 局部变量存在于函数局部命名空间；模块顶层变量属于模块命名空间。

关于 `global`：

- 读取全局变量通常“能看到”，但在函数内部赋值会创建局部变量，除非显式声明 `global x`。
- 课程风格规则（课件强调）：
  - **尽量不要用全局变量**
  - **全局常量是好的**（用 `ALL_CAPS` 命名）
  - 避免 magic numbers（用具名常量替代）

Pylint：

- 静态检查工具，用来发现潜在错误、风格问题，并给重构建议。

## Part B (week3(b)(2).pdf): Python Database Connectivity (MySQL)

### 1) Database / DBMS / SQL Quick Review

- Database：数据集合
- Table：表（行/列）
- DBMS：管理数据库的软件
- SQL：结构化查询语言
  - DDL：建库建表（`CREATE`, `ALTER`, `DROP`）
  - DML：增删改查（`INSERT`, `DELETE`, `UPDATE`, `SELECT`）

### 2) Connecting MySQL From Python

课件示例使用 `mysql.connector`：

- 创建连接：host/user/password
- 创建 cursor：`mycursor = mydb.cursor()`
- 执行 SQL：`mycursor.execute(sql)`

### 3) CRUD And Common Queries

课件覆盖的典型语句：

- `CREATE DATABASE ...`
- `CREATE TABLE ...` / `ALTER TABLE ...`
- `INSERT INTO ... VALUES (%s, %s)`（占位符写法）
- `SELECT * FROM ...`、选择指定列、`fetchall()`
- `WHERE ...`、`ORDER BY ...`
- `DELETE ...`、`UPDATE ...`
- `LIMIT ... OFFSET ...`
- `DROP TABLE IF EXISTS ...`

`commit()` 的意义（课件特别强调）：

- 对数据库有改动（insert/update/delete）后要 `commit()` 才会持久化。
- 不 commit 的改动可能在连接关闭后丢失。

### 4) Security/Quality: Avoid Hardcoding Credentials

课件指出的常见问题：

- 用户名/密码等敏感信息硬编码

给出的解决方案：

- 把连接信息放到 `configfile.ini`
- 用 Python 标准库 `configparser` 读取

### 5) Exercise: Student Information Management

课件末尾的练习题方向：

- 管理 student 信息
- 支持增删改查（思路与 Customers 示例类似）
- 优先考虑：结构清晰、代码可读、信息不硬编码

## SQLite Material (SQLite3_Python_Lecture.pptx + Sample_code_SQLite3.7z)

PPTX 共 6 页，标题结构为：

- SQLite3 in Python
- What is SQLite3?
- Creating a Connection
- Creating a Table
- Summary
- Activity

SQLite 的特点：

- 轻量、单文件数据库（不需要单独安装服务端）
- Python 内置模块 `sqlite3` 即可使用

### Included Sample Project: Week5_1 User Manager

代码在本目录的 [week3_pdf/Week5_1/main.py](week3_pdf/Week5_1/main.py) 等文件中（也来自压缩包）。

- [week3_pdf/Week5_1/database.py](week3_pdf/Week5_1/database.py)
  - `sqlite3.connect("users.db")`
  - `CREATE TABLE IF NOT EXISTS users (...)`

- [week3_pdf/Week5_1/user_manager.py](week3_pdf/Week5_1/user_manager.py)
  - `add_user(name, email)`：插入用户（使用 `?` 占位符，避免拼接 SQL）
  - `view_users()`：查询全部
  - `search_user(name)`：`LIKE` 模糊查找
  - `delete_user(user_id)`：按 id 删除

- [week3_pdf/Week5_1/main.py](week3_pdf/Week5_1/main.py)
  - 命令行菜单循环，调用上面的 CRUD 函数

运行方式（在仓库根目录执行）：

```powershell
cd d:\workshop\MSE800-PSD\week3_pdf\Week5_1
python main.py
```

第一次运行会在当前目录生成 `users.db`。

## Practice Ideas (Using demo_file.txt)

如果你想把 Part A 的“文件处理”练得更扎实，可以用 `demo_file.txt` 做这些小练习：

- 统计总行数/总字符数/总单词数
- 找出出现次数最多的前 N 个单词（忽略大小写与标点）
- 把所有章节标题（全大写行、或满足某个规则的行）抽取出来写到新文件
- 实现一个简单搜索：输入关键词，输出匹配行号与上下文

---

后续你把 Week 3 的任务要求发出来后，我可以把 README 的“Exercises/Tasks”部分补成更贴近作业的 checklist（输入/输出、数据结构、函数拆分、测试点）。
