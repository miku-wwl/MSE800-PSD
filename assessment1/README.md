# MSE800 Assessment 1（中文整理）

本 README 根据 [assessment1/MSE800_Assessment%201%20-%20v1.pdf](MSE800_Assessment%201%20-%20v1.pdf) 整理，目的是把**要求、提交物、注意事项、评分重点**讲清楚，便于你按清单完成。

这是一个**学习版整理**，适合你先理解作业要求、再自己动手完成。为了避免直接拿 AI 结果提交，我另外整理了更偏“自己手搓路线”的说明：[study-guide.md](study-guide.md)。

现在这个目录里还补了一个独立的参考骨架，源码和 SQL 都放在单独文件夹里，方便你边看边改：

- [reference_car_rental/src/car_rental/model/entities.py](reference_car_rental/src/car_rental/model/entities.py)
- [reference_car_rental/src/car_rental/repository/database.py](reference_car_rental/src/car_rental/repository/database.py)
- [reference_car_rental/src/car_rental/repository/user_repository.py](reference_car_rental/src/car_rental/repository/user_repository.py)
- [reference_car_rental/src/car_rental/repository/car_repository.py](reference_car_rental/src/car_rental/repository/car_repository.py)
- [reference_car_rental/src/car_rental/repository/booking_repository.py](reference_car_rental/src/car_rental/repository/booking_repository.py)
- [reference_car_rental/src/car_rental/service/auth_service.py](reference_car_rental/src/car_rental/service/auth_service.py)
- [reference_car_rental/src/car_rental/service/car_service.py](reference_car_rental/src/car_rental/service/car_service.py)
- [reference_car_rental/src/car_rental/service/booking_service.py](reference_car_rental/src/car_rental/service/booking_service.py)
- [reference_car_rental/src/car_rental/controller/app_controller.py](reference_car_rental/src/car_rental/controller/app_controller.py)
- [reference_car_rental/sql/schema.sql](reference_car_rental/sql/schema.sql)
- [reference_car_rental/sql/seed.sql](reference_car_rental/sql/seed.sql)
- [reference_car_rental/sql/queries.sql](reference_car_rental/sql/queries.sql)

## 1. 作业概览

- 课程：MSE800 Professional Software Engineering（Level 8, 30 credits）
- 作业：Assignment 1 — Object-Oriented Programming Assignment
- 性质：个人作业（Individual）
- 课程占比：30%
- 项目主题：实现一个**Car Rental System（汽车租赁系统）**
- 总目标：运用软件工程原则与实践，使用**面向对象（OOP）**、**设计模式**与合适的开发方法，做出一个功能完整、可维护、对用户友好的系统。

## 2. 学习成果映射（LO / GPO）

- Task 1 → LO1, GPO1
- Task 2 与 Task 3 → LO2, GPO4

## 3. 重要注意事项（一定要看）

- **独立完成**：作业用于评估你的知识；学术与职业诚信要求你独立完成。怀疑串通（collusion）会被处理；抄袭相关规则以 Student Handbook 为准。
- **不清楚就问 tutor**：说明里明确写了，指令不清晰要主动询问。
- **提交平台**：在 Blackboard 指定位置提交。
- **反馈时间**：提交后 15 天内返回百分比与反馈。
- **通过条件（Success Criteria）**：
  - 总分必须 **≥ 50%** 才能通过；
  - 还要求：每个 task item 必须达到 PASS。
- **最多 3 次尝试**。
- **迟交/多次尝试的影响很大**：
  - 第二/第三次尝试：需要重做的任务，其对总评的最大贡献会被 **cap 到 50%**。
  - **迟交被视为第二次尝试**，同样会触发 50% cap。

> 截止时间：PDF 页里没有写具体日期，按 Blackboard 的 Due 时间为准。

## 4. 系统功能需求（Car Rental System Requirements）

你实现的系统至少要覆盖以下 4 大块（PDF 明确列出）：

### 4.1 User Management
- 用户注册与登录（registration + login）
- 区分角色：customer 与 admin，并且各自有不同权限

### 4.2 Car Management
- 维护可租车辆数据库（至少包含这些字段）：
  - ID, make, model, year, mileage,
  - available now,
  - minimum rent period, maximum rent period
- 管理员可以对车辆记录进行：新增 / 更新 / 删除（add, update, delete）

### 4.3 Rental Booking
- 客户可以查看可用车辆与详情
- 预订功能：选择车辆、指定租期日期、填写必要信息
- 计算租金：基于车辆、租期、以及额外费用（additional charges）

### 4.4 Rental Management
- 管理员管理预订：批准/拒绝请求（approve / reject）

## 5. 作业任务（Tasks）

### Task 1：Design and Architecture（LO1）
- 设计面向对象架构
- 使用合适的设计模式增强模块化与可维护性（PDF 举例：Factory Method / Singleton / Observer）
- 交付：
  - 高层架构图（high-level architectural diagram）
  - 组件如何交互的说明

### Task 2：Innovative Solutions（LO2）
- 提出一个创新功能/增强点，让系统区别于传统租车系统
- 方向示例：移动端、IoT、云服务、独特用户体验等
- 关键：解释该创新如何满足特定行业需求、带来竞争优势

### Task 3：Software Evolution（LO2）
- 给出系统演进计划：更新、修 bug、新增功能如何做
- 明确策略覆盖：
  - 软件维护（maintenance）
  - 版本管理（versioning）
  - 向后兼容（backward compatibility）
- 强调软件工程原则对长期成功的重要性

## 6. 提交物清单（Submission Requirements）

PDF 明确要求上传以下内容到 Blackboard：

- Source Code Folder：
  - 源代码文件夹 + 必要项目文件
  - 或者一个文本文件，里面放你的源码链接（例如 GitHub repo link）+ 必要项目文件
- Release Build Zip：
  - 把 release build 的可执行文件打包成 zip
- ReadMe：
  - 一个 text/pdf 文件，包含用户文档细节（User Documentation）
- Design and Architecture：
  - 一个 pdf 文件，包含 UML diagrams
- Maintenance and Support：
  - 一个 pdf 文件，包含维护、版本、兼容性策略

## 7. 评分重点（Marking Rubric 摘要）

### 7.1 Task 1（总权重 30%）
- User Documentation（10%）：你的 ReadMe/用户文档要清晰且结构化，目标读者是“用户 + 程序员”。高分要求包含：
  - 配置/安装/运行/操作的步骤指南
  - 所有相关文件都包含，并解释每个文件在系统中的用途
  - README 写清楚发布许可（licensing terms）
  - 已知 bug/问题要记录
  - Credit 区域包含你的开发者信息
- System Documentation（20%）：用于解释设计与架构的 UML 图。
  - A 档要求：同时提供 **Class + Use Case + Sequence** 三种 UML 图
  - B/C 档：允许只提供其中 2 个或 1 个（但会降档）

### 7.2 Task 2（总权重 40%）
- Car Rental System（30%）：
  - A 档：满足全部 4 项功能需求，并提供流畅体验；同时包含创新特性
  - 中档：满足 3/4 或 2/4，可能无创新
- Coding standard（10%）：评价你的代码规范（模块化、封装、性能考虑、注释文档、缩进格式、命名等）

### 7.3 Task 3（总权重 30%）
- Maintenance and Support：演进计划是否覆盖并讲清楚：
  - 维护、版本、向后兼容
  - A 档需要覆盖全部三项策略

## 8. 我认为最重要的“做事顺序”（建议）

1) **先把 4 大功能需求跑通**（注册登录/角色、车辆 CRUD、预订、审批）
2) 再做 Task 1 的架构与 UML：
   - 先画 Class Diagram（类/关系）
   - 再补 Use Case（角色与用例）
   - 再补 Sequence（关键流程：预订/审批/登录等）
3) 再做 Task 2 的创新点（必须写清“行业需求 + 竞争优势”，不是只加一个小功能）
4) 最后写 Task 3 演进计划（维护/版本/兼容）
5) 收尾：
   - README/用户文档补齐 rubric 要求
   - 生成 Release Build Zip（可执行文件）
   - 整理提交包结构（Blackboard 要求的 5 类文件）

## 9. 常见踩坑清单（对照自查）

- README 没写许可（licensing terms）
- README 没写已知问题（known bugs）
- README 没写“每个文件做什么”
- UML 图只画了 1 个（会影响 Task 1 的 20%）
- 功能只做了 customer 端，admin 权限/审批没做（会直接影响“4 项需求”）
- 没有创新点，但文本里又没解释（Task 2 会被扣）
- 没有演进计划（Task 3 会被扣）
- 迟交导致 cap（最亏）

---

如果你愿意，我也可以：

- 根据你现有项目代码结构，帮你把“提交结构/README 模板/运行方式/文件说明”补到最符合 rubric 的版本；
- 或者帮你生成 UML（Class/Use Case/Sequence）的 `.drawio` 模板文件，方便你导出 PDF。
