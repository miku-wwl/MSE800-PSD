**Week 7 — Raw SQLite CRUD + Azure VM + Terraform**

这个目录使用最原始的数据库方案：`sqlite3` + 手写 SQL + repository/service 分层，不使用 ORM。

## 目录内容

- `week7_app/`：Flask + `sqlite3` 的 CRUD 示例。
- `sql/`：`schema.sql`、`seed.sql`、`queries.sql`。
- `tests/`：最小 CRUD 测试。
- `terraform/`：Azure VM 的 Terraform 部署骨架。
- `.github/workflows/`：CI 和部署 workflow。

## 本地运行

```powershell
cd week7
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

## API

- `GET /health`
- `GET /api/products`
- `POST /api/products`
- `GET /api/products/<id>`
- `PUT /api/products/<id>`
- `DELETE /api/products/<id>`

## 测试

```powershell
cd week7
pytest -q
```

## Terraform

Terraform 文件会把 Azure VM、网络、安全组和启动脚本一起定义好，部署过程也通过 Terraform 完成。
