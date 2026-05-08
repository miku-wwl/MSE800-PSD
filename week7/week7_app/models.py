from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Product:
    product_id: int | None
    name: str
    sku: str
    description: str
    quantity: int
    price: float
    created_at: str | None = None

    def to_dict(self) -> dict[str, object]:
        return {
            "product_id": self.product_id,
            "name": self.name,
            "sku": self.sku,
            "description": self.description,
            "quantity": self.quantity,
            "price": self.price,
            "created_at": self.created_at,
        }
