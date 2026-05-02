# 源码参考说明

这份文件是给你自己学习用的，不是提交物。

## 结构

- `src/car_rental/model/entities.py`：实体和枚举
- `src/car_rental/repository/database.py`：数据库连接与初始化
- `src/car_rental/repository/*.py`：数据库访问
- `src/car_rental/service/*.py`：业务规则
- `src/car_rental/controller/app_controller.py`：可运行演示
- `sql/schema.sql`：建表
- `sql/seed.sql`：初始化数据
- `sql/queries.sql`：常用查询

## 你自己改写时建议

- 先改数据结构，再改业务逻辑
- 不要把所有逻辑塞到一个文件
- 先跑通最小流程，再补输入校验和异常处理
- 把注释改成自己的话
