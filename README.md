# flask_api_json_encoder

A JSON encoder that extends `FlaskJSONEncoder` and supports common data types

```python
from flask import Flask
import flask_api_json_encoder

app = Flask(__name__)
flask_api_json_encoder.APIJsonEncoder(app)
```
