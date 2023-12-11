from pathlib import Path
from flask import Flask, jsonify

from db import Repository

app = Flask(__name__)


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    Repository.init_db(db_path=':memory:',
                       schema_path=Path(__file__).parent.joinpath("schema.sql").resolve())

    from controllers.user_controller import *
    from controllers.transaction_controller import *
    from controllers.advice_controller import *

    app.run()
