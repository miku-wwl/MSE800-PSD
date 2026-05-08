# Week 4 Recap (MSE 800)

本目录保存 Week 4 的课件与配套练习。Week 4 的重点可以概括为两条主线：

- **面向对象编程（OOP）与 OO 设计**：从“把相关数据与操作封装进类”出发，学习类/对象/属性/方法，以及 OO 分析与设计（top-down 的 OO design / OOAD）。
- **UML 与交互建模**：通过 **Sequence Diagram（时序图）**理解对象/系统之间的消息交互；并结合练习做简单的 UML 设计与数据库 CRUD 需求分析。

## Files In This Folder

- [week4(a).pdf](week4%28a%29.pdf)
  - 主题：OOP 入门（类/对象/属性/方法），如何“发现/设计”类（例如通过 top-down 设计、从函数参数聚合出对象等），并引入 OOAD 的概念。

- [week4(b).pdf](week4%28b%29.pdf)
  - 主题：OOP 四大核心概念概览（Encapsulation / Abstraction / Inheritance / Polymorphism），并重点讲解 **Inheritance（继承）**与类层次结构（superclass/subclass）。

- [Sequence_Diagram_Software_Development.pptx](Sequence_Diagram_Software_Development.pptx)
  - 主题：Sequence Diagram 基础（Actors、Objects/Classes、Lifelines、Messages、Activation Bars），提供登录流程示例，并给出 best practices 与常见绘图工具。

- [Exercise-week-4.docx](Exercise-week-4.docx)
  - 练习：UML Exercise —— 设计一个 **Library Management System**（管理书籍、成员与借阅流程），要求用 UML 图表达系统能力与核心实体。

- [Exercise-week-4-2.docx](Exercise-week-4-2.docx)
  - 练习：Database Exercise —— 以 Student 信息管理为例，要求用 Python + 数据库实现基本 CRUD（新增、更新、删除等）。

- [Exercise-week-4-2 (1).docx](Exercise-week-4-2%20%281%29.docx)
  - 与上一个 `Exercise-week-4-2.docx` 内容看起来一致（同一份练习的重复拷贝）。

- [solutions for week4 exercises/](solutions%20for%20week4%20exercises/)
  - Week 4 练习的 Python 参考解答（见下文说明）。

- [solutions for week 4 exercises.zip](solutions%20for%20week%204%20exercises.zip)
  - 压缩包内容与 `solutions for week4 exercises/` 相同。

## Week 4 Learning Outcomes

完成 Week 4 复习后，你应该能做到：

- 能解释 OOP 的基本思想：用 **class** 组织数据（attributes/instance variables）与行为（methods）。
- 能从问题描述中识别“候选类”，并为每个类写出关键字段与方法（从 top-down 视角做简单 OO 设计）。
- 能使用继承构建类层次结构，理解 superclass / subclass、继承带来的复用，以及“不要重复字段/行为”的动机。
- 能读懂并画出简单的 Sequence Diagram：参与者、对象生命线、消息与激活条。
- 能根据数据库 CRUD 需求描述，整理出核心表字段与基本操作（新增/查询/更新/删除）。

## OOP Slides (week4(a).pdf + week4(b).pdf)

### 1) Classes / Objects / Methods

- Week4(a) 从“类像记录（records）”切入：把相关变量聚合到一个对象里，再把相关操作写成方法。
- 课件强调“类怎么来”：
  - 从现有函数/参数模式中发现（discovery）
  - 从问题域 top-down 分析（OO design / OOAD）

### 2) Four Fundamental Concepts + Inheritance Focus

- Week4(b) 提到了 OOP 四大概念：
  - Encapsulation
  - Abstraction
  - Inheritance
  - Polymorphism
- 并用人/学生/教职工等例子解释 **继承与类层次结构**。

## Sequence Diagram Material (Sequence_Diagram_Software_Development.pptx)

课件覆盖的要点包括：

- Sequence Diagram 是什么、用来表达什么（对象之间的交互顺序）。
- 关键元素：Actors、Objects/Classes、Lifelines、Messages、Activation Bars。
- 示例场景：User Login（User / Login Page / AuthService / Database）。
- Best practices 与常用工具（用于画时序图）。

## Exercise Solutions (solutions for week4 exercises/)

- [solutions for week4 exercises/exercise2.py](solutions%20for%20week4%20exercises/exercise2.py)
  - 一个简化的“图书馆系统”类设计示例（`LibraryItem` / `Book` / `Magazine` / `Library`），包含基本增删与展示。

- [solutions for week4 exercises/exercise3.py](solutions%20for%20week4%20exercises/exercise3.py)
  - 车辆管理示例：抽象基类 `Vehicle` + 多个子类（`Truck`/`Van`/`Car`），并加入日志与维护检查逻辑。

- [solutions for week4 exercises/example_exercise1.py](solutions%20for%20week4%20exercises/example_exercise1.py)
  - MySQL 学生表的示例代码（含 `configparser` + `mysql.connector`）。
  - 注意：该文件里引用了 `sql_statement` 与 `configfile.ini`，但本目录未提供对应文件；因此更像是“课堂示例片段/思路参考”，运行前需要你补齐 SQL 常量与配置文件。
