from __future__ import annotations

import sqlite3

from ..models import Product


class ProductRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def create(self, product: Product) -> Product:
        cursor = self.conn.execute(
            """
            INSERT INTO products (name, sku, description, quantity, price)
            VALUES (?, ?, ?, ?, ?)
            """,
            (product.name, product.sku, product.description, product.quantity, product.price),
        )
        created = self.get_by_id(cursor.lastrowid)
        if created is None:
            raise LookupError("Created product could not be reloaded")
        return created

    def list_all(self) -> list[Product]:
        rows = self.conn.execute("SELECT * FROM products ORDER BY product_id").fetchall()
        return [self._row_to_product(row) for row in rows]

    def get_by_id(self, product_id: int) -> Product | None:
        row = self.conn.execute(
            "SELECT * FROM products WHERE product_id = ?",
            (product_id,),
        ).fetchone()
        return self._row_to_product(row) if row else None

    def get_by_sku(self, sku: str) -> Product | None:
        row = self.conn.execute(
            "SELECT * FROM products WHERE sku = ?",
            (sku,),
        ).fetchone()
        return self._row_to_product(row) if row else None

    def update(self, product: Product) -> Product:
        self.conn.execute(
            """
            UPDATE products
            SET name = ?, sku = ?, description = ?, quantity = ?, price = ?
            WHERE product_id = ?
            """,
            (product.name, product.sku, product.description, product.quantity, product.price, product.product_id),
        )
        updated = self.get_by_id(product.product_id or 0)
        if updated is None:
            raise LookupError("Product not found")
        return updated

    def delete(self, product_id: int) -> None:
        self.conn.execute("DELETE FROM products WHERE product_id = ?", (product_id,))

    def _row_to_product(self, row: sqlite3.Row) -> Product:
        return Product(
            product_id=row["product_id"],
            name=row["name"],
            sku=row["sku"],
            description=row["description"],
            quantity=row["quantity"],
            price=row["price"],
            created_at=row["created_at"],
        )
