from __future__ import annotations

from flask import Blueprint, current_app, jsonify, request

from .db import get_connection
from .repositories import ProductRepository
from .services import ProductService


api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@api_bp.get("/api/products")
def list_products():
    with get_connection(current_app.config["DB_PATH"]) as conn:
        service = ProductService(ProductRepository(conn))
        products = [product.to_dict() for product in service.list_products()]
        return jsonify(products)


@api_bp.get("/api/products/<int:product_id>")
def get_product(product_id: int):
    with get_connection(current_app.config["DB_PATH"]) as conn:
        service = ProductService(ProductRepository(conn))
        product = service.get_product(product_id)
        return jsonify(product.to_dict())


@api_bp.post("/api/products")
def create_product():
    with get_connection(current_app.config["DB_PATH"]) as conn:
        service = ProductService(ProductRepository(conn))
        product = service.create_product(request.get_json(silent=True) or {})
        return jsonify(product.to_dict()), 201


@api_bp.put("/api/products/<int:product_id>")
def update_product(product_id: int):
    with get_connection(current_app.config["DB_PATH"]) as conn:
        service = ProductService(ProductRepository(conn))
        product = service.update_product(product_id, request.get_json(silent=True) or {})
        return jsonify(product.to_dict())


@api_bp.delete("/api/products/<int:product_id>")
def delete_product(product_id: int):
    with get_connection(current_app.config["DB_PATH"]) as conn:
        service = ProductService(ProductRepository(conn))
        service.delete_product(product_id)
        return "", 204
