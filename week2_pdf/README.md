# Week 2 Recap (MSE 800)

本目录保存了 Week 2 的课件与练习题。下面这份 README 用来把 Week 2 的知识点串起来，并给出与本仓库示例代码的对应关系，方便复习与回看。

## Files In This Folder

- week2(a).pdf
  - Week 2 Part A 课件（从 PPT 导出）。
  - 主题覆盖：Functions, Class/Object/Method, String methods, Formatting, Conditionals/Boolean。

- week2(b)(2).pdf
  - Week 2 Part B 课件（从 PPT 导出）。
  - 主题覆盖：Python lists (index/slice/methods), mutability + aliasing, tuples, dictionaries，以及一组 warm-up Q&A。

- Exercise solutions.pdf
  - Week 2 Exercises（题目与要求）。
  - 练习方向：BMI 计算器、成绩评级、简易图书管理、支出追踪。

- Word guessing Flowchart.png
  - “猜单词/猜字母”小游戏流程图（类似 Hangman 的核心逻辑）。

## What You Should Be Able To Do After Week 2

- 用“抽象 (abstraction)”的思路把重复逻辑封装成函数；理解参数/返回值/作用域。
- 理解 Python 的对象模型：一切皆对象；类是蓝图、对象是实例；方法 (method) 与函数 (function) 的区别。
- 熟练使用常见字符串方法，并能把输入清洗成规范形式。
- 能写清晰的 `if` / `elif` / `else`，理解布尔表达式、比较/逻辑运算符与优先级。
- 能使用列表 (list) 表示“序列/集合”，熟悉索引、切片、常用方法；理解“可变对象 + 引用复制”带来的 aliasing 坑。
- 能使用字典 (dict) 表示 key/value 映射，使用常见 dict 方法完成查找、更新与遍历。

## Part A (week2(a).pdf) Detailed Review

### 1) Functions And Abstraction

- 函数是把“常用步骤”变成可复用模块的工具：输入 (arguments) -> 过程 -> 输出 (return value)。
- 关键概念
  - 参数 (parameter) vs 实参 (argument)
  - `return` 的意义：函数把结果“交还”给调用者
  - 局部变量 (local variables)：只在函数体内有效
  - 过程型函数 vs 返回值函数
    - 过程型：做事（例如打印）
    - 返回值型：计算并返回
- 内置函数示例：`round(x)`, `abs(x)`, `int(x)`。

对应示例代码：
- [tmp/week2/functions_examples.py](tmp/week2/functions_examples.py)

### 2) Classes, Objects, Methods

- Class 是“创建对象的蓝图”，Object 是“类的实例”。
- 每个对象都有自己的状态（实例变量 / attributes）。
- 方法 (method) 是“绑定在对象上的函数”，调用形式通常为 `obj.method(...)`。
- 对比：
  - 函数调用：`function(x)`
  - 方法调用：`obj.method()`（方法里通过 `self` 访问当前对象）

对应示例代码：
- [tmp/week2/class_examples.py](tmp/week2/class_examples.py)

### 3) String Methods + Input Cleaning

- 课件里强调：字符串是不可变 (immutable) 的；字符串方法通常“返回新字符串”。
- 常见字符串方法（课件示例覆盖）：
  - `capitalize()`, `lower()`, `upper()`
  - `find()`
  - `startswith()`
  - `split()`
- 典型应用：把用户输入的姓名规范化（去空格、大小写整理、拆分/拼接）。

对应示例代码：
- [tmp/week2/string_methods_examples.py](tmp/week2/string_methods_examples.py)

### 4) Formatting Output

- 输出不只是 `print(x)`：更常见的是拼出可读的结果字符串。
- 常用方式
  - f-string：`f"value={x:.2f}"`
  - `str.format()`：`"{0:.2f}".format(x)`
- 核心关注点：宽度、精度（保留几位小数）、对齐等。

### 5) Conditionals And Boolean Logic

- `bool` 只有 `True` / `False`。
- 比较运算：`<`, `<=`, `==`, `!=`, `>=`, `>`
- 逻辑运算：`and`, `or`, `not`
- Python 支持链式比较：`low <= x <= high`。
- 风格建议：布尔变量用 `is_...` / `can_...` 等前缀提高可读性。

对应示例代码：
- [tmp/week2/conditionals_examples.py](tmp/week2/conditionals_examples.py)

### 6) Small Applied Practice: Temperature Converter

- 核心点：字符串前缀判断 + 数值解析 + 条件分支 + 格式化输出。

对应示例代码：
- [tmp/week2/temperature_converter.py](tmp/week2/temperature_converter.py)

## Part B (week2(b)(2).pdf) Detailed Review

### 1) Lists (Sequence + Array)

- List 适合表示“可变的序列数据”。
- 重要操作
  - 索引从 0 开始：`a[0]`
  - 负索引：`a[-1]` 表示最后一个
  - `len(a)` 获取长度
- 可变性 (mutable)：修改 `names[1] = "Alex"` 会“原地改变列表”。

### 2) Slicing (Sublist)

- 切片 `a[start:end]` 用于取子序列（`end` 不包含）。
- 还可以对切片赋值，实现批量替换。

### 3) List Operators / Functions / Methods

- 运算符：`list1 + list2`（拼接），`list * n`（重复）。
- 常用函数/方法（按使用频率整理）
  - `append`, `extend`, `insert`
  - `remove`, `pop`
  - `sort`, `reverse`
  - `index`, `count`
- 课件还展示了把字符串列表用 `' '.join(list_of_words)` 拼成一句话的用法。

### 4) The Classic Pitfall: Aliasing

- 重点：Python 变量存的是“对象引用”，`a = b` 只是让两个变量指向同一个 list 对象。
- 后果：对 `a` 的修改会影响 `b`，因为它们是同一个对象。
- 规避思路
  - 需要副本时，用 `b.copy()` 或 `list(b)` 或 `b[:]`（浅拷贝）。

### 5) Tuples (Recap)

- Tuples 类似 list，但不可变。
- 使用场景：固定结构的记录、函数返回多个值等。

### 6) Dictionaries (Key/Value)

- Dict 用于映射关系：`key -> value`。
- 常见操作
  - 创建：`{}`
  - 新增/更新：`d[key] = value`
  - 查询：`d[key]` 或 `d.get(key, default)`
  - 遍历：`for k in d: ...` 或 `for k, v in d.items(): ...`
- 常见方法（课件覆盖）：`clear`, `keys`, `values`, `items` 等。

## Exercises (Exercise solutions.pdf)

练习题的目标不是“记语法”，而是把 Week 2 的函数、条件、列表/字典等组合起来做一个完整小程序。

### Exercise 1: BMI Calculator And Interpretation

- 输入：体重与身高
- 计算 BMI，并按阈值输出分类
  - Underweight: < 18.5
  - Normal: 18.5 - 24.9
  - Overweight: 25 - 29.9
  - Obese: >= 30
- 建议拆分函数
  - `calc_bmi(weight, height) -> bmi`
  - `classify_bmi(bmi) -> label`

### Exercise 2: Grade Classifier (List + Loop + Conditionals)

- 输入格式提示：`[score1, score2, score3, ...]`
- 要求：用列表存储分数并遍历；用条件判断给出 A/B/C/D/F；输出分数保留 1 位小数。
- 建议把“评分规则”写成独立函数，避免重复 if/elif。

### Exercise 3: Simple Book Management System

- 典型功能：添加书籍、删除书籍、查找书籍、展示清单。
- 推荐数据结构
  - 入门版：`list[dict]`（每本书一个 dict：title/author/year...）
  - 或者：用 dict 做索引（例如 title -> book_info）
- 练习重点：循环菜单 + 输入处理 + 列表/字典操作。

### Exercise 4: Expense Tracker

- 典型功能：记录支出（金额/类别/备注/日期），按类别汇总，输出统计结果。
- 推荐数据结构
  - `list[dict]` 存明细
  - `dict[category] = total` 做聚合
- 练习重点：把数据“收集 -> 存储 -> 分析 -> 输出”。

## Word Guessing Flowchart (Word guessing Flowchart.png)

流程图表达的是一个经典的“猜字母”循环：

- 初始化
  - 随机生成一个单词 `secret`
  - 生成同长度的空白占位（例如 `"_ _ _"` 或 `['_', '_', '_']`）
  - 初始化生命值 `lives`
- 循环直到胜利/失败
  - 让用户输入一个字母 `guess`
  - 如果 `guess` 在 `secret` 中：把所有匹配位置的空白替换为该字母
  - 否则：`lives -= 1`
  - 如果空白全部被填满：胜利
  - 如果生命值用尽：失败

实现时常见的加分点：
- 处理重复猜测（用 `set` 记住已猜过的字母）
- 输入校验（必须是单个字母、非空等）

## Related Code In This Repo (Optional But Useful)

- Week 2 Part A 的配套示例（函数/字符串/类/条件/温度转换）：
  - [tmp/week2/README.md](tmp/week2/README.md)
- 与“类 + 列表 + 排序”相关的小练习：
  - [week2/activity2/main.py](week2/activity2/main.py)
- 与运算符/数学函数相关的小练习：
  - [week2/activity1/math.py](week2/activity1/math.py)
