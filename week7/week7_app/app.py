from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, jsonify

from .config import DEFAULT_DB_PATH
from .db import initialize_database


def create_app(db_path: Path | str | None = None) -> Flask:
    app = Flask(__name__)
    app.config["DB_PATH"] = Path(db_path or os.environ.get("WEEK7_DB_PATH", DEFAULT_DB_PATH))
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")

    initialize_database(app.config["DB_PATH"])

    from .routes import api_bp

    app.register_blueprint(api_bp)

    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(LookupError)
    def handle_lookup_error(error: LookupError):
        return jsonify({"error": str(error)}), 404

    return app
