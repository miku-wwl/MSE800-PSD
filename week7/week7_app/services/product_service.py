from __future__ import annotations

from ..models import Product
from ..repositories import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def list_products(self) -> list[Product]:
        return self.repository.list_all()

    def get_product(self, product_id: int) -> Product:
        product = self.repository.get_by_id(product_id)
        if product is None:
            raise LookupError("Product not found")
        return product

    def create_product(self, payload: dict[str, object]) -> Product:
        product = self._build_product(payload)
        if self.repository.get_by_sku(product.sku):
            raise ValueError("SKU already exists")
        return self.repository.create(product)

    def update_product(self, product_id: int, payload: dict[str, object]) -> Product:
        self.get_product(product_id)
        product = self._build_product(payload, product_id=product_id)
        existing = self.repository.get_by_sku(product.sku)
        if existing and existing.product_id != product_id:
            raise ValueError("SKU already exists")
        return self.repository.update(product)

    def delete_product(self, product_id: int) -> None:
        self.get_product(product_id)
        self.repository.delete(product_id)

    def _build_product(self, payload: dict[str, object], *, product_id: int | None = None) -> Product:
        if not isinstance(payload, dict):
            raise ValueError("JSON body is required")

        name = str(payload.get("name", "")).strip()
        sku = str(payload.get("sku", "")).strip()
        description = str(payload.get("description", "")).strip()
        quantity = self._coerce_int(payload.get("quantity", 0), field_name="quantity")
        price = self._coerce_float(payload.get("price", 0), field_name="price")

        if not name:
            raise ValueError("name is required")
        if not sku:
            raise ValueError("sku is required")
        if quantity < 0:
            raise ValueError("quantity must be greater than or equal to 0")
        if price < 0:
            raise ValueError("price must be greater than or equal to 0")

        return Product(
            product_id=product_id,
            name=name,
            sku=sku,
            description=description,
            quantity=quantity,
            price=price,
        )

    @staticmethod
    def _coerce_int(value: object, *, field_name: str) -> int:
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{field_name} must be an integer") from exc

    @staticmethod
    def _coerce_float(value: object, *, field_name: str) -> float:
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{field_name} must be a number") from exc
