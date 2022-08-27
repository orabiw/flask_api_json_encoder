""" Api JSON encoder

A JSON encoder that extends `FlaskJSONEncoder` and supports common data types


```python
from flask import Flask
import flask_api_json_encoder

def create_app() -> Flask:
    app = Flask(__name__)
    flask_api_json_encoder.APIJsonEncoder(app)
    return app
```
"""
__version__ = "0.2.0"

from flask_api_json_encoder.extension import APIJsonEncoder  # noqa:F401
from flask_api_json_encoder.json_encoder import JSONEncoder  # noqa:F401
