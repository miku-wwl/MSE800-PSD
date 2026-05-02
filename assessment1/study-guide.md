# Assessment 1 学习版作业拆解

这份文档的目标不是“替你交作业”，而是帮你把这份 Assessment 拆成可以自己完成的步骤。你后面要手搓，就按这里的顺序做。

## 1. 先明确：你要交什么

PDF 里明确要求的提交物有 5 类：

- 源码文件夹，或者源码链接文本
- Release build zip
- ReadMe / User Documentation
- Design and Architecture PDF（UML 图）
- Maintenance and Support PDF（维护、版本、兼容性）

所以你真正要准备的是两层内容：

- **代码层**：Car Rental System 的功能实现
- **文档层**：把系统怎么用、怎么设计、怎么维护写清楚

## 2. 你要自己完成的系统功能

PDF 要求的系统至少覆盖这 4 块：

### 2.1 用户管理

- 注册
- 登录
- 角色区分：customer 和 admin

你自己实现时可以这样想：

- customer 负责查看车辆、下单、查看自己的租赁
- admin 负责管理车辆、审核订单

### 2.2 车辆管理

- 车辆信息要能保存
- 字段至少包含：ID、make、model、year、mileage、available now、minimum rent period、maximum rent period
- admin 要能新增、修改、删除车辆

### 2.3 预订流程

- customer 能看见可用车辆
- customer 能选车、填日期、提交预订
- 系统要能算租金

### 2.4 订单管理

- admin 可以批准
- admin 可以拒绝

## 3. 建议的实现顺序

不要一上来就写 UI。先按下面顺序做，最稳：

1. 设计数据结构
2. 设计核心类
3. 先实现登录/角色
4. 再实现车辆 CRUD
5. 再实现预订与租金计算
6. 再实现管理员审核
7. 最后补文档和 UML

## 4. Task 1 怎么自己写

Task 1 的重点不是“画得多漂亮”，而是**能说明系统结构**。

### 4.1 你应该有的内容

- 一个高层架构图
- 每个模块怎么 взаимодействовать 的说明
- 至少一个或多个设计模式的说明

PDF 举例提到的模式：

- Factory Method
- Singleton
- Observer

### 4.2 建议你这样组织

- Model / Entity：User、Car、Booking
- Service：AuthService、CarService、BookingService
- Repository / Data Access：负责存取数据
- Controller / UI：负责输入输出

### 4.3 你可以写的说明角度

- 为什么要把登录和业务逻辑分开
- 为什么车辆管理要单独成模块
- 为什么预订流程和租金计算要单独封装
- 设计模式解决了什么问题

## 5. Task 2 怎么自己写

Task 2 要的是“创新点”，不是普通功能堆叠。

### 5.1 你可以从这几个方向想

- 移动端体验
- 云端同步
- IoT 车辆状态
- 智能推荐
- 动态定价

### 5.2 写作时一定要回答两个问题

- 这个创新解决了什么行业需求
- 它为什么比传统做法更有竞争力

### 5.3 你写的时候要避免

- 只说“我加了一个功能”
- 没有解释业务价值
- 没有说明对客户或 admin 的帮助

## 6. Task 3 怎么自己写

Task 3 是软件演进计划，核心是三件事：

- 维护
- 版本管理
- 向后兼容

### 6.1 可以写的维护内容

- bug 修复流程
- 测试策略
- 日志与监控
- 备份与恢复

### 6.2 可以写的版本管理内容

- 语义化版本号
- 版本发布说明
- 功能分阶段上线

### 6.3 可以写的兼容性内容

- 保持旧数据可读
- API / 接口兼容
- 数据库迁移策略

## 7. 你自己的 README 应该包含什么

PDF 的 rubric 对 ReadMe 写得很明确。你自己写的时候，至少要包含：

- 安装步骤
- 配置步骤
- 启动步骤
- 操作步骤
- 文件说明
- 许可说明
- 已知问题
- 开发者信息

如果你后面真要提交，这一块很容易丢分，所以建议单独检查。

## 8. UML 图怎么自己准备

至少准备这 3 种：

- Class Diagram
- Use Case Diagram
- Sequence Diagram

建议你自己先写文字，再画图：

- 先列类
- 再列角色和用例
- 再挑 1 到 2 个关键流程画时序图

## 9. 一个适合自学的目录想法

如果你后面要自己做，可以按这个思路组织：

- src/：源码
- sql/：数据库脚本
- docs/：文档
- docs/uml/：UML 图
- docs/maintenance/：维护说明
- docs/readme/：用户说明

如果你想先看一个最小参考骨架，可以直接对照这些文件：

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

## 10. 自检清单

你写完后，自己问自己这 8 个问题：

- 我有没有实现注册和登录？
- 我有没有区分 customer 和 admin？
- 我有没有车辆 CRUD？
- 我有没有预订流程？
- 我有没有租金计算？
- 我有没有审批流程？
- 我有没有 3 种 UML？
- 我有没有写维护、版本、兼容性？

## 11. 最后提醒

这份作业最重要的不是“把字写满”，而是：

- 逻辑完整
- 结构清楚
- 功能对题
- 文档对 rubric

你如果后面要手搓，建议先把 Task 1 的类图和流程图画出来，再开始编码。这样最不容易返工。