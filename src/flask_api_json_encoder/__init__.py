""" Api JSON encoder

A JSON encoder that extends `FlaskJSONEncoder` and supports common data types


```python
from common_flask_json_encoder import Encoder as JSONEncoder


def create_app() -> Flask:
    app = Flask(__name__)
    app.json_encoder = JSONEncoder
    return app
```

"""
__version__ = "0.1.0"

from flask_api_json_encoder.extension import APIJsonEncoder  # noqa:F401
