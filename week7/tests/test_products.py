from __future__ import annotations

import tempfile
from pathlib import Path

from week7_app.app import create_app


def _make_client():
    temp_dir = tempfile.TemporaryDirectory()
    db_path = Path(temp_dir.name) / "test.db"
    app = create_app(db_path=db_path)
    app.config["TESTING"] = True
    return temp_dir, app.test_client()


def test_health_endpoint():
    temp_dir, client = _make_client()
    try:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}
    finally:
        temp_dir.cleanup()


def test_crud_flow():
    temp_dir, client = _make_client()
    try:
        create_response = client.post(
            "/api/products",
            json={
                "name": "Demo Mouse",
                "sku": "SKU-2001",
                "description": "Wireless mouse",
                "quantity": 20,
                "price": 25.5,
            },
        )
        assert create_response.status_code == 201
        created = create_response.get_json()
        assert created["name"] == "Demo Mouse"

        list_response = client.get("/api/products")
        assert list_response.status_code == 200
        products = list_response.get_json()
        assert any(product["sku"] == "SKU-2001" for product in products)

        product_id = created["product_id"]
        update_response = client.put(
            f"/api/products/{product_id}",
            json={
                "name": "Demo Mouse Pro",
                "sku": "SKU-2001",
                "description": "Wireless mouse upgraded",
                "quantity": 18,
                "price": 29.9,
            },
        )
        assert update_response.status_code == 200
        assert update_response.get_json()["name"] == "Demo Mouse Pro"

        delete_response = client.delete(f"/api/products/{product_id}")
        assert delete_response.status_code == 204

        get_response = client.get(f"/api/products/{product_id}")
        assert get_response.status_code == 404
    finally:
        temp_dir.cleanup()


def test_invalid_payload_is_rejected():
    temp_dir, client = _make_client()
    try:
        response = client.post("/api/products", json={"name": "", "sku": ""})
        assert response.status_code == 400
    finally:
        temp_dir.cleanup()
